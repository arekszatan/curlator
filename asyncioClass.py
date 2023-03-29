import logging
import asyncssh as asyncssh
import asyncio
import qasync
from PySide6.QtCore import Signal


class Asyncio:
    startedSendCurl = Signal()
    finishedSendCurl = Signal()
    connectionOK = Signal()
    error = Signal()
    outputCmd = Signal(str)
    errorSendCurl = Signal()

    @qasync.asyncSlot()
    async def runAsyncioCmdLiveLog(self, ip, username, password, cmd):  # Live log phs
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password), timeout=3) as conn:
                result = await conn.run(cmd, check=True)
                self.outputCmd.emit(result.stdout)
        except:
            self.outputCmd.emit("Brak logów")
            logging.exception(f'Error to get result with {cmd} for {ip} as {username}')

    @qasync.asyncSlot()
    async def checkConnectionSSH(self, ip, username, password, cmd):  # First connection to ssh
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password),
                                              timeout=3) as conn:
                result = await conn.run(cmd, check=True)
                self.connectionOK.emit()
        except:
            logging.exception(f'Can not connect to {ip} as {username}')
            self.error.emit()

    async def sendAsyncioCurl(self, ip, username, password, cmd):  # Send curl asynch
        self.startedSendCurl.emit()
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password), timeout=3) as conn:
                result = await conn.run(cmd, check=True)
                self.finishedSendCurl.emit()
        except:
            self.errorSendCurl.emit()
            logging.exception(f'Can not send curl {cmd} to {ip}')



