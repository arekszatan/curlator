import logging

import qasync
import asyncio
from PySide6.QtCore import Signal


class Asyncio:
    started = Signal()
    finished = Signal()
    outputCmd = Signal(list)

    @qasync.asyncSlot()
    async def runAsyncioCmd(self, cmd):
        self.started.emit()
        proc = await asyncio.create_subprocess_shell(
            cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE)

        stdout, stderr = await proc.communicate()
        logging.debug(f'[{cmd!r} exited with {proc.returncode}]')
        if stdout:
            separator = bytes("\n", 'utf-8')
            splitedOutput = stdout.split(separator)
            self.outputCmd.emit(splitedOutput)
            #logging.debug(f'[stdout]\n{stdout.decode()}')
        if stderr:
            logging.debug(f'[stderr]\n{stderr.decode()}')
        self.finished.emit()
