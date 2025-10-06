"""
Sulthon duduk terdiam di kelas. Semua orang sudah beramai-ramai meninggalkan kelas, namun dia tetap tegak di bangkunya, matanya tertuju pada kertas yang ada di atas mejanya.

Permasalahan tersebut terpampar jelas di bawah ancaman tersebut:

Kamu menepuk bahu Sulthon; tidak mengefek. Kertas ancaman tersebut tampak basah dari keringat yang mengucur dari tubuh Sulthon. Sepertinya dia benar-benar membutuhkan bantuan. Bisakah kamu membantunya?

Input Format

Determine(n)
Constraints

n	: integer
 dan jika  memenuhi suatu syarat unik, dia pasti bagian dari pola tersebut.

Apakah syarat unik tersebut? Perhatikan polanya saja.

Output Format

"Ya" | "Tidak"
Sample Input 0

Determine(3)
Sample Output 0

Ya
Explanation 0

Kamu memberi tahu kepada Sulthon bahwa  adalah salah satu bilangan yang benar. Dia menatapmu dengan sinis.

Sample Input 1

Determine(4)
Sample Output 1

Tidak
Explanation 1

Kamu juga memberi tahu kepada Sulthon bahwa  bukanlah bilangan yang termasuk pola tersebut. Dia tak merespon, tetapi tangannya sudah mengepal.
"""
def Determine(n:int)->str:
    if n>0:
        if n%2==0:
            if n>2:
                return "Tidak"
            elif n==2:
                return "Ya"
        elif n%3==0:
            if n>3:
                return "Tidak"
            elif n==3:
                return "Ya"
        elif n%5==0:
            if n>5:
                return "Tidak"
            elif n==5:
                return "Ya"
        elif n%7==0:
            if n>7:
                return "Tidak"
            elif n==7:
                return "Ya"
        else:
            return "Ya"
            
#JANGAN DIUBAH!
print(eval(input()))