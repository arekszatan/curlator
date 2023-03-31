import logging
import aiofiles as aiofiles
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
    curlCallBackSignal = Signal(str)
    logLocalHostSignal = Signal(list)
    logLocalHostSignalCurl = Signal(list)

    def __init__(self):
        self.conn = None

    @qasync.asyncSlot()
    async def runAsyncioCmdLiveLog(self, ip, username, password):  # Live log phs
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password), timeout=3) as conn:
                self.conn = conn
                while True:
                    await asyncio.sleep(0.1)
        except:
            logging.exception(f'Error connection for {ip} as {username}')

    @qasync.asyncSlot()
    async def displayCdmLiveLog(self, cmd):
        try:
            result = await self.conn.run(cmd, check=True)
            self.outputCmd.emit(result.stdout)
        except:
            self.outputCmd.emit("Brak logów")
            logging.exception(f'Error to get result with {cmd}')

    @qasync.asyncSlot()
    async def checkConnectionSSH(self, ip, username, password):  # First connection to ssh
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password),
                                              timeout=3) as conn:
                self.connectionOK.emit()
        except:
            logging.exception(f'Can not connect to {ip} as {username}')
            self.error.emit()

    @qasync.asyncSlot()
    async def sendAsyncioCurl(self, ip, username, password, cmd):  # Send curl asynch
        self.startedSendCurl.emit()
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password), timeout=3) as conn:
                await conn.run(cmd, check=True)
                self.finishedSendCurl.emit()
        except:
            self.errorSendCurl.emit()
            logging.exception(f'Can not send curl {cmd} to {ip}')

    @qasync.asyncSlot()
    async def getCurlCallBack(self, ip, username, password, cmd, delay):  # Send curl asynch
        try:
            async with await asyncio.wait_for(asyncssh.connect(ip, username=username, password=password),
                                              timeout=3) as conn:
                await asyncio.sleep(delay)
                result = await conn.run(cmd, check=True)
                self.curlCallBackSignal.emit(result.stdout)
        except:
            logging.exception(f'Can not get call back curl info for {cmd} to {ip}')

    @qasync.asyncSlot()
    async def readFileOfLogs(self, filePath):
        try:
            async with aiofiles.open(filePath, mode='r') as f:
                lines = await f.readlines()
                self.logLocalHostSignal.emit(lines)
                await f.close()
        except:
            await f.close()
            logging.exception(f'Error cant open and read file {filePath}')

    @qasync.asyncSlot()
    async def sendLocalCurl(self, cmd):
        self.startedSendCurl.emit()
        try:
            await asyncio.create_subprocess_shell(cmd, stdout=asyncio.subprocess.PIPE)
            self.finishedSendCurl.emit()
        except:
            self.errorSendCurl.emit()
            logging.exception(f'Error cant send local curl  {cmd}')

    @qasync.asyncSlot()
    async def getCurlCallBackLocal(self, filePath, delay):  # Send curl asynch
        try:
            await asyncio.sleep(delay)
            async with aiofiles.open(filePath, mode='r') as f:
                lines = await f.readlines()
                self.logLocalHostSignalCurl.emit(lines)
                await f.close()
        except:
            logging.exception(f'Error cant open and read file {filePath}')
