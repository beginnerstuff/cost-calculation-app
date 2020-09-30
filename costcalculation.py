print("AYLIK MASRAF HESAP UYG. HOŞGELDİNİZ\nBaşlamadan önce birkaç soruya yanıt vermek zorundasınız")

defkira = input("Kiradamı oturuyorsunuz (evet yada hayır):")
if defkira == "evet":
    kirabedel = int(input("kira ücretiniz nedir:$"))
elif defkira == "hayır":
    print("evinizin kira olmaması size büyük kolaylık sağlar")
    kirabedel = int(0)

defmarriage = input("Medeni haliniz(evli yada bekar):")

if defmarriage == "bekar":
    print("bekarlık sultanlıktır ;)")
    partnerpay = 0
    childnumber = -1
elif defmarriage == "evli":
    partnerpay = int(input("Eşinizin geliri nedir:$"))
    defchild = input("Çocuğunuz varmı (evet yada hayır):")
    if defchild == "evet":
        childnumber = int(input("Kaç çocuğunuz var?:"))
    elif defchild == "hayır":
        childnumber = 0

gelir = int(input("Aylık geliriniz nedir:$"))

mutfak = int(input("Aylık mutfak masrafınız nedir ort:$"))

elektirik = int(input("Aylık elektirik faturanız:$"))
su = int(input("Aylık su faturanız:$"))
doğalgaz = int(input("Aylık doğalgaz faturanız:$"))

definternet = input("Evinizde internet varmi?(evet yada hayır):")

if definternet == "hayır":
    print("bu bir masraf olarak görülmemeli bu çağımızda bir ihtiyaç :)")
    internetf = 0
elif definternet == "evet":
    internetf = int(input("İnternet faturanız nedir:$"))

telefonf = int(input("Kişi başı ort telefon faturanız nedir:$"))

fatura = int(elektirik + su + doğalgaz + internetf + (childnumber + 2) * telefonf)

aylıkmasraf = int((fatura + mutfak) + kirabedel)

gelirtop = (partnerpay + gelir)

kalan = (gelirtop - aylıkmasraf)

print("\n\nAYLIK ORT. MASRAFINIZ :", aylıkmasraf, "$dDIR")
print("\nAYLIK ORT GELİRİNİZ : ", gelirtop, "$dır")
print("\nAY SONU DURUMUNUZ :", kalan, "$dır")

input("\nçıkmak için bir tuşa basınız.")
