__all__: list[str] = []

import cv2
import cv2.typing
import typing as _typing


# Classes
class HfsSegment(cv2.Algorithm):
    # Functions
    def setSegEgbThresholdI(self, c: float) -> None: ...

    def getSegEgbThresholdI(self) -> float: ...

    def setMinRegionSizeI(self, n: int) -> None: ...

    def getMinRegionSizeI(self) -> int: ...

    def setSegEgbThresholdII(self, c: float) -> None: ...

    def getSegEgbThresholdII(self) -> float: ...

    def setMinRegionSizeII(self, n: int) -> None: ...

    def getMinRegionSizeII(self) -> int: ...

    def setSpatialWeight(self, w: float) -> None: ...

    def getSpatialWeight(self) -> float: ...

    def setSlicSpixelSize(self, n: int) -> None: ...

    def getSlicSpixelSize(self) -> int: ...

    def setNumSlicIter(self, n: int) -> None: ...

    def getNumSlicIter(self) -> int: ...

    @_typing.overload
    def performSegmentGpu(self, src: cv2.typing.MatLike, ifDraw: bool = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def performSegmentGpu(self, src: cv2.UMat, ifDraw: bool = ...) -> cv2.typing.MatLike: ...

    @_typing.overload
    def performSegmentCpu(self, src: cv2.typing.MatLike, ifDraw: bool = ...) -> cv2.typing.MatLike: ...
    @_typing.overload
    def performSegmentCpu(self, src: cv2.UMat, ifDraw: bool = ...) -> cv2.typing.MatLike: ...

    @classmethod
    def create(cls, height: int, width: int, segEgbThresholdI: float = ..., minRegionSizeI: int = ..., segEgbThresholdII: float = ..., minRegionSizeII: int = ..., spatialWeight: float = ..., slicSpixelSize: int = ..., numSlicIter: int = ...) -> HfsSegment: ...



