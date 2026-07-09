const fs = require('fs');
const path = require('path');

const repoDir = 'd:/pj/xx/ai-gen-quiz';
function readLines(file) { return fs.readFileSync(path.join(repoDir, file), 'utf8').split('\n'); }
function writeLines(file, lines) { fs.writeFileSync(path.join(repoDir, file), lines.join('\n'), 'utf8'); }

// part_42
let p42 = readLines('mondai2_ordering/csv_filled/set_1_daily/part_42.csv');
p42[13] = `でなくてなんだろう,Nでなくてなんだろう,①彼女のためなら死んでもいいとまで思う。これが愛でなくて何だろう。,家族のために5時間もかけて料理を作る、これが愛でなくてなんだろう。,家族のために,5時間もかけて,料理を作る、,これが愛,でなくて,なんだろう。,"Cấu trúc 'Nでなくてなんだろう' là câu hỏi tu từ mang tính khẳng định tuyệt đối 'Nếu đây không phải là N thì còn có thể là gì nữa'."`;
p42[15] = `てのこと,V－てのこと,①彼が6年も留学できたのは、親の援助があってのことだ。,家族が幸せに暮らせるのもお父さんの頑張りがあってのことだ。,家族が,幸せに,暮らせるのも、,お父さんの頑張りが,あって,のことだ。,"Mẫu 'V-てのこと' dùng để nhấn mạnh rằng vế trước có được hoàn toàn là nhờ vào hành động hoặc điều kiện ở vế V phía sau."`;
p42[18] = `ては,Vのでは,①そんなに遠くから通勤していらっしゃるのでは大変ですね。,毎日小さなことで喧嘩しているのでは一緒に暮らすのは難しい。,毎日,小さなことで,喧嘩して,いるのでは、,一緒に暮らすのは,難しい。,"Cấu trúc 'Vのでは' được dùng để đưa ra một thực tế khách quan làm tiền đề lý do, dẫn đến một đánh giá tiêu cực hoặc một khó khăn ở vế sau."`;
writeLines('mondai2_ordering/csv_filled/set_1_daily/part_42.csv', p42);

// part_45
let p45 = readLines('mondai2_ordering/csv_filled/set_1_daily/part_45.csv');
p45[1] = `ても,いくら～ても,①いくら華やかな職業でも、つらいことはたくさんある。,この料理は、いくらレシピ通りに作っても母の味にはならない。,この料理は、,いくら,レシピ通りに,作っても,母の味には,ならない。,"Cấu trúc đi liền ""いくら...ても"" (cho dù... bao nhiêu)."`;
p45[2] = `ても, どんなに～ても,①このコンピュータはどんなに複雑な問題でも解いてしまう。,私は、どんなに仕事が忙しくても毎日家族に電話をかけている。,私は、,どんなに,仕事が,忙しくても,毎日家族に,電話をかけている。,"""どんなに"" đi với tính từ đuôi i thể ても là ""忙しくても"" để tạo nghĩa biểu thị mức độ cực đoan."`;
p45[3] = `ても, 疑問詞～ても,①だれが電話してきても、取りつがないでください。,誰が何と言っても、私はこの服を絶対に買いたい。,誰が,何と,言っても、,私はこの服を,絶対に,買いたい。,"Từ để hỏi ""何"" kết hợp với trợ từ ""と"" và động từ ""言う"" chia thể ても thành ""何と言っても"" tạo trạng ngữ cố định."`;
p45[4] = `ても, どうV－ても,①どう言ってみても、硬の決心を変えさせることはできなかった。,昨日のことは、どう考えても彼女が怒っている理由がわからない。,昨日のことは、,どう,考えても、,彼女が,怒っている理由が,わからない。,"""どう考えても"" là cụm trạng từ đi liền nhau mang nghĩa ""dù có nghĩ thế nào đi nữa""."`;
p45[6] = `ても, ～ても～たろう,①たとえ、努力しても合格できなかっただろう。,あの店の商品なら、たとえ安くてもそんな高いバッグは買わなかっただろう。,あの店の商品なら、,たとえ,安くても,そんな高いバッグは,買わなかった,だろう。,"""たとえ"" thường mở đầu đi kèm với thể ""ても"" (安くても) ở Chunk 2 để giả định tình huống."`;
p45[11] = `でも1,,①友達はプールヘ泳ぎに行った。でも、わたしはアルバイトで行けなかった。,このTシャツを買いたいです。でも、値段が少し高いですね。,このTシャツを買いたいです。,でも、,値段が,少し,高い,ですね。,"""でも"" đứng đầu câu thứ hai làm liên từ biểu thị quan hệ nghịch đối."`;
p45[15] = `でも2,NでもありNでもある NaでもありNaでもある AくもありAくもある,①彼はこの会社の創始者でもあり、今の社長でもある。,彼は私の親友でもあり、良き相談相手でもある。,彼は,私の,親友でもあり、,良き相談,相手でも,ある。,"Mẫu song hành ""AでもありBでもある"" biểu thị tính chất kép của chủ ngữ."`;
writeLines('mondai2_ordering/csv_filled/set_1_daily/part_45.csv', p45);

// part_48
let p48 = readLines('mondai2_ordering/csv_filled/set_1_daily/part_48.csv');
p48[14] = `というと,というと,N3,①A：この企画は大筋はいいが､細かいところで少々無理があるね。B：というと。A：今から説明するよ。,兄が「明日の旅行は中止だ」と言ったので、私は「というと」と聞き返しました。,兄が,「明日の旅行は中止だ」,と言ったので、,私は,「というと」,と聞き返しました。,"Mệnh đề nguyên nhân lý do làm tiền đề. Cụm từ hỏi làm rõ thông tin 「「というと」」 đóng vai trò làm nội dung lời thoại đi kèm."`;
writeLines('mondai2_ordering/csv_filled/set_1_daily/part_48.csv', p48);

// part_39 (Missing Diacritics)
let p39 = readLines('mondai2_ordering/csv_filled/set_1_daily/part_39.csv');
let vi = [
    '"Sau danh từ 「私の実家」, sử dụng 「つまり」 (tóm lại/có nghĩa là) để giải thích lại một cách rõ ràng."',
    '"Dùng 「つまり」 để tóm tắt lại tình huống phía trước, dẫn đến kết luận ở cuối câu."',
    '"Động từ thể từ điển 「行く」 kết hợp với danh từ 「つもり」 chỉ dự định và 「です」 tạo thành mẫu câu cơ bản."',
    '"Động từ thể từ điển 「買う」 đi với 「つもりはない」 thể hiện ý chí phủ định mạnh mẽ (hoàn toàn không có ý định mua)."',
    '"Động từ thể từ điển 「言う」 đi với 「つもりではなかった」 phủ định ý định trong quá khứ."',
    '"Động từ thể từ điển 「買う」 đi với 「つもりで」 thể hiện hành động tiếp theo được thực hiện với mục đích nhất định."',
    '"Tính từ 「いい」 kết hợp trực tiếp với 「つもりだ」 thể hiện niềm tin chủ quan của bản thân."',
    '"Danh từ đi kèm trợ từ の 「二十代の」 kết nối với 「つもりで」 thể hiện việc bản thân cứ ngỡ như là thực tế."',
    '"Động từ thể Ta 「言った」 đi với 「つもりはない」 khẳng định bản thân không hề có ác ý hay ý định đó trong quá khứ."',
    '"Động từ thể Ta 「した」 đi với 「つもりで」 giả định như thể đã thực hiện hành động đó."',
    '"Động từ chia ở thể Te liên tiếp 「起きて」 và 「して」 tạo thành chuỗi hành động theo thứ tự thời gian."',
    '"Tính từ đuôi na 「楽しみ」 lặp lại hai lần kèm trợ từ 「で」 để nhấn mạnh cảm xúc cực độ."',
    '"Sử dụng 「で」 ở đầu câu để chuyển tiếp chủ đề câu chuyện một cách tự nhiên trong giao tiếp."',
    '"Danh từ 「大雨」 đi với trợ từ 「で」 biểu thị nguyên nhân, dẫn đến kết quả tàu trễ."',
    '"Động từ thể Te 「焼いて」 kết hợp với 「あげました」 thể hiện hành động làm ơn cho người khác một cách tự nguyện."',
    '"Động từ thể Te 「抱っこして」 đi với 「あげて」 tạo thành lời yêu cầu, nhờ vả nhẹ nhàng."',
    '"Tha động từ thể Te 「冷やして」 kết hợp với 「あります」 thể hiện trạng thái đã được chuẩn bị sẵn và vẫn đang duy trì."',
    '"Danh từ 「肉」 và 「魚」 đi kèm 「であれ」 tạo thành cấu trúc song hành (cho dù là A hay B thì cũng)."',
    '"Danh từ 「平日」 và 「週末」 kết hợp với 「であろうと」 thể hiện sự thật không thay đổi bất kể điều kiện nào."',
    '"Danh từ 「雨」 kết hợp với 「であろうとなかろうと」 mang nghĩa nhượng bộ tuyệt đối (dù có hay không có cũng không thay đổi)."'
];
for(let i=1; i<=20; i++){
    if(!p39[i]) continue;
    let parts = p39[i].split(',');
    // The last part is explanation. We can just replace the last element.
    // Wait, the original explanation in part_39 might have commas, so it's surrounded by quotes.
    // Let's use parseCsvLine
    let cols = parseCsvLine(p39[i]);
    cols[10] = vi[i-1];
    p39[i] = stringify(cols);
}
writeLines('mondai2_ordering/csv_filled/set_1_daily/part_39.csv', p39);

console.log('Hardcode fixes complete!');
