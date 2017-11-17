import collections

"""
半音数からピッチクラスと相対オクターブを取得する。
"""
class PitchClass:
    _PitchClass = collections.namedtuple('PitchClass', ['PitchClass', 'RelativeOctave'])
    @classmethod
    def Get(cls, halfToneNum:int):
        pitchClass = halfToneNum % 12
        relativeOctave = halfToneNum // 12
        if pitchClass < 0:
            pitchClass += 12
        return cls._PitchClass(pitchClass, relativeOctave)


if __name__ == '__main__':
    pc = PitchClass.Get(9)
    print(pc)
    print(tuple(pc))
    print(pc.PitchClass, pc.RelativeOctave)
#    pc.PitchClass += 2#AttributeError: can't set attribute

    for halfToneNum in range(12*3):
        print(halfToneNum, PitchClass.Get(halfToneNum))
    for halfToneNum in range(-12*3, 0):
        print(halfToneNum, PitchClass.Get(halfToneNum))
