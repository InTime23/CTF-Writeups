from Crypto.Util.number import bytes_to_long, long_to_bytes, GCD


c_hex = "0x9982edb224e7a0bb4b581bddc454bd26b56358bcafc50a08fb84fd07128ac818597145ad1246dd005c62fa3831e0cc2d432e5e1f98047610a801037c43d0fb7d09bf8a2f1d8db266643fb088c428ad9ef0e9304780c5d06ecdccc0b602c2aee63e1d1670050d53ca4473aba20b411135b44f01df20328c70d57e89bb26a74ab1"
c = int(c_hex, 16)
e = 0x10001


m1 = 50
ct1_hex = "0xee8c46c08920756fa14fdc10c86d36b825fb33ad5ea457c19d9cd16d7cd686bfc59b5cb24daad1972e61abc80bf381e0235fd205e29ddebe92ff5d82617ab213a6db59993efa81c61f61d250720fac34a179470c91a4334e84150d65d7fb979416b05760dccd6ef4d92adb7b5ac7b722e56905c4470b1d7ef5b9b12f551f206a" # Output after entering \x02
ct1 = int(ct1_hex, 16)

m2 = 51
ct2_hex = "0x704ce06412b9c09332d423f0f6c472d9f66e0e115dff93c212033c3562766cb52bc1fcf92888f75a088ac0e14fbef52f464faaa9f0f4c46768de2c1a0ba232d96a8bb505a62d253b7aedf5473f83d644f8405de6c26ad9d466983c65bdf0e22af355779c17fb4f01493f69a0e0af787227261e66b4fa5633d48583ce8f9ac8de" # Output after entering \x03
ct2 = int(ct2_hex, 16)


# Since m^e = k*n + ct, then (m^e - ct) is a multiple of n
n = GCD(pow(m1, e) - ct1, pow(m2, e) - ct2)

print(f"Recovered n: {n}")

#(Since n is prime, phi is n-1)
phi = n - 1
d = pow(e, -1, phi)
flag_long = pow(c, d, n)

print(f"Flag: {long_to_bytes(flag_long).decode()}")
