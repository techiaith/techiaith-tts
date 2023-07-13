"""
Normaliser demo
"""
from techiaith.tts.testun.normaliser import parse_text


def _parse_user_input():
    history = []
    while True:
        text = input("\nprompt: ")
        if text in ["exit", "cau"]:
            # exit loop if keyword used
            break
        clean_text = parse_text(text)
        print("\nresult:", clean_text)


if __name__ == "__main__":
    print(
        """
                  cccc
           codxkkkOOOOkkkxdol
        ldkO0000000000000000Okdlc
      lxO0K000000000000000000000kdc
    cx00000000OkxxxxxkkO0000000000Oo
   lk00000Oxolc        codk000000000xc
  lk0000Oxl               cok00000000xc
 cx0000ko                   cx00000000o
 oO000Oo                     cx0000000d
 d0000d                       cdO0000xl
 d000Oo                         lodol
 oO000o  Uned Technolegau Iaith
 cx000xc     Normaleiddiwr       cc
  lk000d                        clc
   lk000xc                     loc
    cdO00Odl                codoc
      cdk00Okdlc        clodxdl
         ldxO00Okkxxxxxkkxdoc
            cllodddoooolc

Teipiwch 'cau' i gau'r brompt."""
    )
    _parse_user_input()
