import csv

new_lines = {
    6: 'なる,R－そうになる,N4,①叱られて泣きそうになった。,息子は転んで泣きそうになった。,息子は,転んで,泣き,そうに,なった,。,"Cấu trúc R-そうになる (suýt nữa thì). Động từ bỏ masu + そうになる. Chủ ngữ 息子は đi kèm với hành động nguyên nhân 転んで, dẫn đến trạng thái 泣きそうになった."\n',
    7: 'なる,となる,N3,①彼はまだ20歳なのに、もうすぐ一児の父となります。,彼はまだ20歳なのに、もうすぐ一児の父となります。,彼はまだ20歳なのに、,もうすぐ,一児の,父と,なります,。,"Trợ từ と dùng với động từ なります để chỉ sự trở thành, biến đổi. Trạng từ もうすぐ chỉ thời gian, và 一児の父 hợp thành tân ngữ. Câu thể hiện sự chuyển biến trạng thái rõ rệt."\n',
    8: 'なる,～となると→【となると1】、【となると2】Nともなると,N2,①3月ともなるとだいぶ暖かく感じられるようになります。,週末ともなるとあのスーパーは買い物客で大混雑します。,週末,ともなると,あのスーパーは,買い物客で,大混雑します,。,"Danh từ thời gian 週末 đi với mẫu ともなると để đưa ra một mốc thời gian đặc biệt. Theo sau là chủ ngữ あのスーパーは và nguyên nhân 買い物客で dẫn đến trạng thái đông đúc."\n',
    9: 'なる,～になる　Nになる　V一ることになる,N4,①来年から5月4日は休校日になります。,うちの娘は、来年からいよいよ高校生になります。,うちの娘は、,来年から,いよいよ,高校生に,なり,ます。,"Trạng từ thời gian 来年から và phó từ いよいよ đi trước danh từ bổ ngữ. Danh từ 高校生 đi với trợ từ に và động từ なる ở dạng lịch sự để chỉ sự thay đổi."\n',
    10: 'なる,Nになると,N3,①国語なら教えられるが、数学になると全く手がでない。,毎年のことですが、冬になると電気代が急に高くなります。,毎年のことですが、,冬に,なると,電気代が,急に高くなります,。,"Cấu trúc điều kiện 冬になると (hễ đến mùa đông) đặt ở đầu vế câu. Theo sau là chủ ngữ 電気代が và phó từ 急に bổ nghĩa cho tính từ chỉ sự biến động."\n',
    11: 'なる,おR－になる,N4,①先生はお帰りになりました。,田中さん、もう本日の夕食はお買いになりましたか。,田中さん、もう,本日の,夕食は,お買いに,なり,ましたか。,"Cụm danh từ tân ngữ 本日の夕食は đứng trước cấu trúc tôn kính ngữ. Động từ 買う chuyển sang dạng bỏ masu là 買い, bọc bởi お...になる để thể hiện sự lịch sự."\n',
    12: 'なるたけ,,N4,①この仕事はなるたけ早く仕上げて下さい。,今日は用事があるので、なるたけ早く家に戻ってきてね。,今日は用事があるので、,なるたけ,早く,家に,戻ってきて,ね。,"Phó từ なるたけ (cố gắng hết sức trong khả năng) đi trước để bổ nghĩa cho trạng từ 早く. Tiếp theo là cụm trạng ngữ chỉ địa điểm 家に và động từ hành động 戻ってきて."\n',
    13: 'なるべく,なるべく,N4,①今晩はなるべく早めに帰ってきて下さいね。,体調管理のために、なるべく野菜を多く食べるようにしています。,体調管理のために、,なるべく,野菜を,多く,食べるようにしています,。,"Từ chỉ mức độ なるべく đứng trước cụm tân ngữ 野菜を và trạng từ 多く để nhấn mạnh mục tiêu. Theo sau là động từ 食べる đi với cấu trúc thói quen ようにしています."\n',
    14: 'なるべく,なるべくなら,N3,①なるべくなら、今晩は早く帰って休みたい。,休みの日は、なるべくなら静かなカフェでゆっくり過ごしたい。,休みの日は、,なるべくなら,静かな,カフェで,ゆっくり過ごしたい,。,"Liên từ なるべくなら (nếu được thì...) đặt ở đầu vế để thể hiện nguyện vọng lý tưởng. Sau đó là định ngữ 静かな bổ nghĩa cho danh từ địa điểm カフェで."\n',
    15: 'なるほど,,N4,①いい店だとは聞いていたが、なるほどサービスもいいし料理もうまい。,友人が勧めてくれた通り、なるほどこの店のパンは非常に美味しい。,友人が勧めてくれた通り、,なるほど,この店の,パンは,非常に美味しい,。,"Thán từ/Phó từ なるほど biểu thị sự đồng tình, nhận ra sự thật sau khi trải nghiệm. Nó đứng trước cụm chủ ngữ この店のパンは và phó từ chỉ mức độ 非常に."\n',
    16: 'なれた,R－なれたN,N3,①使いなれた道具を使う。,毎日の料理には、使いなれた包丁が一番安全で便利です。,毎日の料理には、,使い,なれた,包丁が,一番安全で便利です,。,"Động từ bỏ masu 使い kết hợp với phụ từ なれた để tạo thành một tính từ căn bản mang nghĩa đã quen dùng. Cụm này bổ nghĩa trực tiếp cho danh từ 包丁が."\n',
    17: 'なんか,なんか,N4,①A：なんかたべるものない？B：冷蔵庫見てみたら？なんか入っていると思うけど。,この部屋に入ると、なんか甘い匂いがしてきませんか。,この部屋に入ると、,なんか,甘い,匂いが,してきませんか,。,"Từ đệm/Phó từ なんか (hình như, có cái gì đó) dùng trong văn nói hằng ngày để biểu thị cảm giác mơ hồ. Nó đi trước cụm tính từ + danh từ 甘い匂いが."\n',
    18: 'なんか,なんか＜様子＞,N4,①彼女と話しているとなんかほっとした気持ちになる。,最近忙しかったから、今日はなんか少しのんびりしたい気分です。,最近忙しかったから、,今日は,なんか,少し,のんびりしたい気分です,。,"Chủ ngữ thời gian 今日 là trợ từ は đi trước phó từ chỉ tâm trạng なんか. Theo sau là phó từ chỉ mức độ 少し bổ nghĩa cho trạng thái mong muốn のんびりしたい."\n',
    19: 'なんか,～かなんか　N／A／V　かなんか,N3,①今度の休みは映画かなんか行かない？,お腹が空いたから、パンかなんか買ってきてくれない？,お腹が空いたから、,パン,かなんか,買ってきて,くれ,ない？,"Cấu trúc かなんか (hay cái gì đó đại loại thế) đứng sau danh từ パン để gợi ý chung chung. Trình tự tự nhiên đi với động từ nhờ vả 買ってきてくれない."\n',
    20: 'なんか,Nやなんか,N3,①スポーツは好きですが、野球やなんかの球技はあまり得意ではないんですよ。,本やなんかの重い荷物は、全部箱に入れてください。,本,やなんかの,重い,荷物は、,全部箱に入れて,ください。,"Cấu trúc やなんかの đi sau danh từ 本 để liệt kê đại diện. Theo sau là định ngữ 重い bổ nghĩa cho danh từ 荷物は, tạo thành chủ ngữ cho mệnh đề cầu khiến."\n'
}

with open('mondai2_ordering/csv_filled/set_1_daily/part_67.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in new_lines.items():
    if idx < len(lines):
        lines[idx] = line

with open('mondai2_ordering/csv_filled/set_1_daily/part_67.csv', 'w', encoding='utf-8') as f:
    f.writelines(lines)
