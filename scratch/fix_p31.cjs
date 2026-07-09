const fs = require('fs');
const path = require('path');
const repoDir = 'd:/pj/xx/ai-gen-quiz';
function readLines(file) { return fs.readFileSync(path.join(repoDir, file), 'utf8').split('\n'); }
function writeLines(file, lines) { fs.writeFileSync(path.join(repoDir, file), lines.join('\n'), 'utf8'); }

let p31 = readLines('mondai2_ordering/csv_filled/set_1_daily/part_31.csv');
p31[14] = `たかが,たかが,①そんなに悔しがらないでたかがゲームのことじゃないか。,そんなに悔しがらないで、たかがゲームのことじゃないか。,そんなに悔しがらないで、,たかが,ゲームの,こと,じゃ,ないか。,"たかが là một phó từ có nghĩa là 'chỉ là', 'chỉ có', được dùng để đánh giá thấp hoặc coi nhẹ."`;
p31[15] = `たかが,たかが～ぐらいで／ごときで,①仲良くしてよたかがお菓子ひとつぐらいで喧嘩しないで。,仲良くしてよ、たかがお菓子ひとつぐらいで喧嘩しないで。,仲良くしてよ、,たかが,お菓子,ひとつぐらいで,喧嘩し,ないで。,"たかが～ぐらいで biểu thị sự việc nhỏ nhặt không đáng để làm to chuyện."`;
p31[16] = `たかだか,たかだか,①駅前のスーパーまではたかだか歩いて5分ぐらいです。,駅前のスーパーまでは、たかだか歩いて5分ぐらいです。,駅前のスーパーまでは、,たかだか,歩いて,5分,ぐらい,です。,"たかだか là phó từ mang ý nghĩa 'nhiều nhất cũng chỉ', thể hiện số lượng/mức độ không đáng kể."`;
p31[17] = `だから,丁寧な形に「ですから」がある。だから＜帰結＞,①踏切で事故があった。だから、学校に遅刻してしまった。,朝寝坊した。だから、約束の電車に乗り遅れた。,朝寝坊した。,だから、,約束の,電車に,乗り,遅れた。,"Liên từ 'だから' đặt ở đầu câu thứ hai đóng vai trò nối kết biểu thị kết quả tất yếu xảy ra."`;
p31[18] = `だから,だから ～のだ／～わけだ,①A：ジャクソンさんは、小学生の時からもう10年も日本語を習っているそうです。B：だから、あんなに日本語が上手なんですね。,毎日練習しているんだね。だから、料理が上手なわけだ。,毎日練習しているんだね。,だから、,料理が,上手な,わけ,だ。,"Liên từ 'だから' đứng đầu câu sau phối hợp chặt chẽ với cấu trúc kết luận hiển nhiên '～わけだ' (Thảo nào mà/Bảo sao mà)."`;
writeLines('mondai2_ordering/csv_filled/set_1_daily/part_31.csv', p31);

console.log('Fixed p31!');
