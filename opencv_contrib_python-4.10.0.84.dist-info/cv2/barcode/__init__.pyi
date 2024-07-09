__all__: list[str] = []

import cv2
import cv2.typing
import typing as _typing


# Classes
class BarcodeDetector(cv2.GraphicalCodeDetector):
    # Functions
    @_typing.overload
    def __init__(self) -> None: ...
    @_typing.overload
    def __init__(self, prototxt_path: str, model_path: str) -> None: ...

    @_typing.overload
    def decodeWithType(self, img: cv2.typing.MatLike, points: cv2.typing.MatLike) -> tuple[bool, _typing.Sequence[str], _typing.Sequence[str]]: ...
    @_typing.overload
    def decodeWithType(self, img: cv2.UMat, points: cv2.UMat) -> tuple[bool, _typing.Sequence[str], _typing.Sequence[str]]: ...

    @_typing.overload
    def detectAndDecodeWithType(self, img: cv2.typing.MatLike, points: cv2.typing.MatLike | None = ...) -> tuple[bool, _typing.Sequence[str], _typing.Sequence[str], cv2.typing.MatLike]: ...
    @_typing.overload
    def detectAndDecodeWithType(self, img: cv2.UMat, points: cv2.UMat | None = ...) -> tuple[bool, _typing.Sequence[str], _typing.Sequence[str], cv2.UMat]: ...

    def getDownsamplingThreshold(self) -> float: ...

    def setDownsamplingThreshold(self, thresh: float) -> BarcodeDetector: ...

    def getDetectorScales(self) -> _typing.Sequence[float]: ...

    def setDetectorScales(self, sizes: _typing.Sequence[float]) -> BarcodeDetector: ...

    def getGradientThreshold(self) -> float: ...

    def setGradientThreshold(self, thresh: float) -> BarcodeDetector: ...



