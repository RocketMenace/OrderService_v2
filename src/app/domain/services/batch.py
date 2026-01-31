from typing import AsyncGenerator

from app.domain.entities.batch import Batch
from app.domain.value_objects import BatchID, OrderLine


class BatchService:
    async def allocate(self, *, line: OrderLine, batches: list[Batch]) -> BatchID:
        batch = await anext(self._find_batches(line=line, batches=batches))
        await batch.allocate(line=line)
        return batch.reference

    async def _find_batches(
        self,
        line: OrderLine,
        batches: list[Batch],
    ) -> AsyncGenerator[Batch, None]:
        for batch in sorted(batches):
            if await batch.can_allocate(line=line):
                yield batch
