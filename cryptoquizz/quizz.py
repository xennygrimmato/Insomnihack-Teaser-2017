mp = {'Adi Shamir': 1952,
'Alex Biryukov': 1969,
'Amos Fiat': 1956,
'Antoine Joux': 1967,
'Arjen K. Lenstra': 1956,
'Claus-Peter Schnorr': 1943,
'Dan Boneh': 1969,
'Daniel Bleichenbacher': 1964,
'Daniel J. Bernstein': 1971,
'David Naccache': 1967,
'Donald Davies': 1924,
'Douglas Stinson': 1956,
'Eli Biham': 1960,
'Horst Feistel': 1915,
'Jacques Patarin': 1965,
'Jacques Stern': 1949,
'Jim Massey': 1934,
'Joan Daemen': 1965,
'Kaisa Nyberg': 1948,
'Lars Knudsen': 1962,
'Markus Jakobsson': 1968,
'Martin Hellman': 1945,
'Michael O. Rabin': 1931,
'Mitsuru Matsui': 1961,
'Moni Naor': 1961,
'Niels Ferguson': 1965,
'Nigel P. Smart': 1967,
'Paul Kocher': 1973,
'Paul van Oorschot': 1962,
'Paulo Barreto': 1965,
'Phil Rogaway': 1962,
'Rafail Ostrovsky': 1963,
'Ralph Merkle': 1952,
'Ron Rivest': 1947,
'Ronald Cramer': 1968,
'Ross Anderson': 1956,
'Serge Vaudenay': 1968,
'Shai Halevi': 1966,
'Tatsuaki Okamoto': 1952,
'Victor S. Miller': 1947,
'Whitfield Diffie': 1944,
'Xuejia Lai': 1954,
'Yehuda Lindell': 1971,
'Yvo Desmedt': 1956}


new_mp = {}

for name in mp:
    new_mp[name.split()[-1]] = str(mp[name])

# print new_mp

import socket
def netcat(hostname="quizz.teaser.insomnihack.ch", port=1031, content="1956"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    # s.sendall(str(content))
    # s.shutdown(socket.SHUT_WR)
    # data = s.recv(351)
    from time import sleep
    while True:
        new_data = s.recv(4096)
        print repr(new_data)
        # print l
        try:
            for key in new_mp.keys():
                if key in repr(new_data):
                    s.sendall((new_mp[key]+"\n").encode())
                    print "Sending: {0}".format(mp[lname])
                    break
        except:
            pass
        if not new_data:
            print(repr(new_data))
            break
    s.shutdown(socket.SHUT_WR)
    s.close()

netcat()
