filename = input("Enter a filename: ").strip()
infile = open(filename, "r")

counts = 26 * [0]

for line in infile:
    line = line.lower()
    for ch in line:
        if "a" <= ch <= "z":
            counts[ord(ch) - ord("a")] += 1

infile.close()

for i in range(len(counts)):
    if counts[i] != 0:
        print(chr(ord('a') + i) + " appears " + str(counts[i]) + (" time" if counts[i] == 1 else " times"))