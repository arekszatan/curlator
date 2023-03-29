import logging
import threading
from socket import socket

import asyncssh as asyncssh
import asyncio
import qasync
from PySide6.QtCore import Signal


class Asyncio:
    started = Signal()
    finished = Signal()
    connectionOK = Signal()
    error = Signal()
    outputCmd = Signal(str)

    @qasync.asyncSlot()
    async def runAsyncioCmd(self, ip, username, password, cmd):
        self.started.emit()
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password), timeout=3) as conn:
                result = await conn.run(cmd, check=True)
                self.outputCmd.emit(result.stdout)
        except:
            self.outputCmd.emit("")
            logging.exception(f'Can not connect to {ip} as {username}')
            self.error.emit()
        self.finished.emit()

    @qasync.asyncSlot()
    async def checkConnectionSSH(self, ip, username, password, cmd):
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password),
                                              timeout=3) as conn:
                result = await conn.run(cmd, check=True)
                self.connectionOK.emit()
        except:
            logging.exception(f'Can not connect to {ip} as {username}')
            self.error.emit()


