text = """hm al, mo tmh hm al, huvh gn hul jzlnhgmt:
qulhulo 'hgn tmaxlo gt hul cgty hm nzrrlo
hul nxgtsn vty voomqn mr mzhovslmzn rmohztl,
mo hm hvel vocn vsvgtnh v nlv mr homzaxln
vty ak mppmngts lty hulc?
hm ygl: hm nxllp;
tm cmol; vty, ak v nxllp hm nvk ql lty
hul ulvoh-vwul vty hul humznvty tvhzovx numwen
huvh rxlnu gn ulgo hm, 'hgn v wmtnzccvhgmt
yldmzhxk hm al qgnu'y. hm ygl, hm nxllp;
hm nxllp: plowuvtwl hm yolvc: vk, hulol'n hul oza;
rmo gt huvh nxllp mr ylvhu quvh yolvcn cvk wmcl
qult ql uvdl nuzrrxly mrr hugn cmohvx wmgx,
cznh sgdl zn pvznl  """

alphabet = "abcdefghijklmnopqrstuvwxyz"


def find_freq():
    count_arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for ch in text:
        if ch.isalpha():
            count_arr[alphabet.find(ch)] += 1
    for freq_num, ch in zip(count_arr, alphabet):
        print(freq_num, ch)


find_freq()

