# Make your code as unreadable as possible
So to make dream real, I've created this mini program, numbers logic I did by my self, but for arguments and vars thank for https://pyob.oxyry.com/

# How to use
Write in console:
`python obfuscate.py <filename> <power (optional, default: 50)> <times (optional, default: 1)>`

# Example
Code in:
```py
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    i = 0
    while nums:
        current_element = nums.pop(0)
        i += 1

        sub_target = target - current_element

        if sub_target in nums:
            return [i - 1, nums.index(sub_target) + i]

print(two_sum([3, 2, 4], 6))
```
Code out (jic I'm using ruff formatter):
```py
from typing import List


def two_sum(OOOOO000OOO00000O: List[int], O0OOO0OO0O0O0000O: int) -> List[int]:
    OO000O0O0000O0000 = (
        -((839397803725990748085860474166602 + 1117585860185035484910323242166) // 736)
        + (938957061031624938312572203178634 + 912729225742819674852207510790) // 823
    ) // ((-613475959807899000709326128966 + 613475959807899000709326290702) // 184)
    while OOOOO000OOO00000O:
        O0O0OO00OO0O000OO = OOOOO000OOO00000O.pop(
            (
                (414627732262414431518658428767436 - 260508523093214343505591980856)
                // 740
                - (379164925205228972280928184668961 + 485044653230196968738873900365)
                // 678
            )
            // -(
                (1094536069234595045059434034441 - 1094536069234595045059434137167)
                // -878
            )
        )
        OO000O0O0000O0000 += (
            (-525506581251693981063927439010270 - 1026863298895739443612576070746)
            // -654
            - (108823219539958769502314771508462 - 135123187772818021400548307637)
            // 135
        ) // ((612320586950185528106147516250 - 612320586950185528106148140170) // -880)
        O000OOOO0OO0OO0O0 = O0OOO0OO0O0O0000O - O0O0OO00OO0O000OO
        if O000OOOO0OO0OO0O0 in OOOOO000OOO00000O:
            return [
                OO000O0O0000O0000
                - (
                    (-54939139594097793851269272722251 - 528384290358904743464863761065)
                    // -796
                    - (
                        23563859697114627501257244995203
                        + 267664383895662598490336382851
                    )
                    // 342
                )
                // -(
                    (260673455395567648595825551423 - 260673455395567648595825762239)
                    // -576
                ),
                OOOOO000OOO00000O.index(O000OOOO0OO0OO0O0) + OO000O0O0000O0000,
            ]


print(
    two_sum(
        [
            (
                (-18655997934290006091581934207169 + 1056436237008451533855435890863)
                // -654
                - (-13023409895493334441350679095694 + 187032327292567585027223684179)
                // -477
            )
            // -(
                (-833903975227372626839674622131 + 833903975227372626839674611339)
                // -71
            ),
            (
                -(
                    (321726006505632991825268417694965 - 912499251815115537574465532759)
                    // 369
                )
                + (-850233722086187049396338721353425 - 52484131248947919012728073671)
                // -978
            )
            // -(
                (-480286867883937803878588658840 + 480286867883937803878588947995)
                // 555
            ),
            (
                (761109713748336661231425138710610 - 423443557733522801279712621364)
                // 718
                - (136339540283512387826102652945704 - 729731670145811615714610480296)
                // 128
            )
            // (
                (538033633753761070898672289022 - 538033633753761070898672334046)
                // -336
            ),
        ],
        (
            (-50541934031950062452147098041155 - 279873645315986617421740252357) // -948
            - (-52428098634128696307565293773400 - 538089113908072132027550451456)
            // -988
        )
        // -((-706493371230255896099859688225 + 706493371230255896099860363809) // 928),
    )
)
```