def vis(do_kolk):
    vsi = []
    for i in range(do_kolk):
        arr=[]
        del11 = float(input("vnesi prvi racunski del: "))
        del12 = float(input("vnesi drugi racunski del: "))
        del21 = float(input("vnesi teorijo: "))
        if i == 0:
            arr.append(((4*del11 + del12)/170.0)*100.0)
            arr.append((del21 / 100.0)*100.0)
            print("Teorija: {:.2f}% Praksa: {:.2f}% Skupaj: {:.2f}%".format(arr[1], arr[0], float(arr[0] + arr[1])/2.0))
    
        elif i == 1:
            arr.append(((4*del11 + del12)/170.0)*100.0)
            arr.append((del21 / 62.0)*100.0)
            print("Teorija: {:.2f}% Praksa: {:.2f}% Skupaj: {:.2f}%".format(arr[1], arr[0], float(arr[0] + arr[1])/2.0))
        
        elif i == 2:
            arr.append(((4*del11 + del12)/170.0)*100.0)
            arr.append((del21 / 100.0)*100.0)
            print("Teorija: {:.2f}% Praksa: {:.2f}% Skupaj: {:.2f}%".format(arr[1], arr[0], float(arr[0] + arr[1])/2.0))
        
        elif i == 3:
            arr.append(((4*del11 + del12)/170.0)*100.0)
            arr.append((del21 / 100.0)*100.0)
            print("Teorija: {:.2f}% Praksa: {:.2f}% Skupaj: {:.2f}%".format(arr[1], arr[0], float(arr[0] + arr[1])/2.0))
        
        elif i == 4:
            arr.append(((4*del11 + del12)/170.0)*100.0)
            arr.append((del21 / 100.0)*100.0)
            print("Teorija: {:.2f}% Praksa: {:.2f}% Skupaj: {:.2f}%".format(arr[1], arr[0], float(arr[0] + arr[1])/2.0))

        vsi.append(arr)
    teorija = 0
    praksa = 0
    for i in range(do_kolk):
        teorija += vsi[i][1]
        praksa += vsi[i][0]
    teorija_procent = teorija / float(do_kolk)
    praksa_procent = praksa / float(do_kolk)
    skupaj_procent = (teorija_procent + praksa_procent) / 2.0
    print("Teorija vsi: {:.2f}% Praksa vsi: {:.2f}% Skupaj vsi: {:.2f}%".format(teorija_procent, praksa_procent, skupaj_procent))
    

    # Račun priporočil 
    teorije_do_zdaj = 0
    racunski_do_zdaj = 0
   
    for j in range(do_kolk):
        teorije_do_zdaj += vsi[j][1]
        racunski_do_zdaj += vsi[j][0]

    skupaj_do_zdaj = teorije_do_zdaj + racunski_do_zdaj

    if do_kolk == 5:
        if racunski_do_zdaj < 250:
            print("Več sreče naslednje leto")
            return
        if teorije_do_zdaj < 250:
            print("Treba bo na teoretični izpit :(")
            return
    else:
        da_naredis_teorijo_rabis = (250.0 - teorije_do_zdaj) / (5 - do_kolk)
        da_naredis_prakso_rabis = (250.0 - racunski_do_zdaj) / (5 - do_kolk) 
        da_naredis_skupaj_rabis = (500 - skupaj_do_zdaj) / (10 - 2*do_kolk)
        if da_naredis_teorijo_rabis < 0:
            da_naredis_teorijo_rabis = 0
        if da_naredis_prakso_rabis < 0:
            da_naredis_prakso_rabis = 0
        if da_naredis_skupaj_rabis < 0:
            da_naredis_skupaj_rabis = 0
    print("Naslednje teoretične kolokvije rabiš pisat: {:.2f}%".format(da_naredis_teorijo_rabis))
    print("Naslednje računske kolokvije rabiš pisat: {:.2f}%".format(da_naredis_prakso_rabis))
    print("Naslednje kolokvije rabiš pisat skupaj: {:.2f}%".format(da_naredis_skupaj_rabis))
    return

def irz(do_kolk):
    return

def opb(do_kolk):
    vsi = []
    vsi_procenti = 0
    for i in range(do_kolk):
        kol = float(input("vnesi točke: "))
        if kol < 25:
            print("Več sreče naslednje leto")
            return
        vsi.append(kol)
        vsi_procenti += kol
    
    if do_kolk == 3:
        if vsi_procenti >= 150.0:
            print("Naredil si")
    else:
        da_naredis_rabis = (150.0 - vsi_procenti) / (3 - do_kolk)
        if da_naredis_rabis < 25:
            da_naredis_rabis = 25  # ker mora bit nad 25
        print("Na naslednjih kolokvijih moraš v povprečju pisati {:.2f}% da narediš".format(da_naredis_rabis))
        
    return 
    

def main():
    vrsta_predmeta = str(input("Kater predmet (vis, irz, opb): "))
    do_koliko_kolokvijev = int(input("Koliko kolokvijev boš vnesel: "))
    if vrsta_predmeta == "vis":
        vis(do_koliko_kolokvijev)
    elif vrsta_predmeta == "irz":
        irz(do_koliko_kolokvijev)
    elif vrsta_predmeta == "opb":
        opb(do_koliko_kolokvijev)
    else:
        print("Napačen vnos")
    return


if (__name__ == "__main__"):
    main()