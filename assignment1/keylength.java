/*
CSC 440
HW1
5
Ximan Liu
*/

public class keylength {
	public static void main(String[] args) {
		String ciphertext = "XVMRNEBXPAEWBZQCDLMOEGSVBYFPAWKKZRSDMKSLOMAKKAAFDWZMZVFPDFWLPMKROWBUDHYYZZWUWDAOEGIKLKBVGHNCBZPAMFFYEWQKDSSSDLPIBYDPPVRLJWEZWDVKESOXPVDQHYPQPMKRWECELQZIVTUUDKTRJMVTOQRZYJAKXIRPSTELJKGFXNQIPGEXKRUZBLXEAVPRSLSEFVERORFNMGEROCAKHIPRDHZSVWDYHFCLJKQEWAUVCVKVLZVYFVEHHSORUEHYXVKVIWHSCKSHNVMCDPSUAUKFTVPOWEYXIFMIWDSFCBWJCCOQBZGHNWICTQOEEXIGWDSQHVCLBFCZOPWJVQKAVKRXSRMOAXWSUAOBLOHSNKKEGYLYEROJDERKSDPAMROHYEZZPSLRBPVREKWGSVUOOEOLJXMCOEUVYFAEOVQYWVDFWRKFPLFFXLOIXVRLZVDGWXIZQDIEOUAHAFIICIPSNSARLYKRJVPLIEEUPLTOZMVXDMIRYWQQKFPLIKPUQWCROHMKSHUHWEWAJVYEKXPVUPFPTQCXWSUAOBEKAIVTUUDKTRJVMCBEBXTQOXMRGKBGZRNMUGOAAVYWWXQFQOOEOKQQIEHNFFC";
		for (int shift = 1; shift <= 14; shift++) {
			int coincidenceCount = 0;
			for (int index = 0; index <= ciphertext.length() - 1; index++) {
				int shiftedIndex = (index + shift) % ciphertext.length();
				if (ciphertext.charAt(index) == ciphertext.charAt(shiftedIndex)) {
					coincidenceCount++;
				}
			}
			System.out.println(shift + ", " +  coincidenceCount);
		}
	}
}