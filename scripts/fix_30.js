import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const BASE_DIR = path.join(__dirname, '..');

// 1. Fix part_67.csv
const p67 = path.join(BASE_DIR, 'mondai2_ordering/csv_cleaned/set_1_daily/part_67.csv');
let txt67 = fs.readFileSync(p67, 'utf8');
txt67 = txt67.replace('なる,R－そうになる,N4,①叱られて泣きそうになった。,R－そうになるN4①叱られて泣きそうになった。` -> Let me use original reference text exactly:,R－そうになる,N4,①叱られて泣きそうになった。` -> Let me use original reference text exactly:,,,,\n', '');
txt67 = txt67.replace('なる,～となると→【となると1】、【となると2】Nともなると,N2,①3月ともなるとだいぶ暖かく感じられるようになります。,となるN3①彼はまだ20歳なのに、もうすぐ一児の父となります。`,となる,N3,①彼はまだ20歳なのに、もうすぐ一児の父となります。`,,,,\n', '');
fs.writeFileSync(p67, txt67);
console.log('Fixed part_67.csv');

// 2. Fix part_72.csv
const p72 = path.join(BASE_DIR, 'mondai2_ordering/csv_cleaned/set_1_daily/part_72.csv');
let txt72 = fs.readFileSync(p72, 'utf8');
const old72 = `にしてみれば,Nにしてみれば,N2,①今何の歌がはやっているかなんて、私にしてみればどうでもいいことだ。それよりもっと大切なことが山ほどある。,"店主にしてみれば、毎日通ってくれる常連客は本当にありがたい存在だ。Cụm 「個人経営の」 (kinh doanh cá thể) bổ nghĩa cho danh từ 「店主」 (chủ tiệm). Danh từ này kết hợp cấu trúc đứng từ lập trường 「にしてみれば」 (đối với/xét từ góc độ của...) tạo thành vế đầu. Vế sau bắt đầu bằng định ngữ 「毎日通ってくれる」 (lui tới mỗi ngày cho) bổ nghĩa cho chủ ngữ 「常連客は」 (khách quen), kết thúc bằng cụm vị ngữ 「本当にありがたい存在だ」 (thật sự là sự tồn tại đáng trân quý).",店主に,してみれば、,毎日通ってくれる,常連客は,本当にありがたい存在だ。,"Cụm 「個人経営の」 (kinh doanh cá thể) bổ nghĩa cho danh từ 「店主」 (chủ tiệm). Danh từ này kết hợp cấu trúc đứng từ lập trường 「にしてみれば」 (đối với/xét từ góc độ của...) tạo thành vế đầu. Vế sau bắt đầu bằng định ngữ 「毎日通ってくれる」 (lui tới mỗi ngày cho) bổ nghĩa cho chủ ngữ 「常連客は」 (khách quen), kết thúc bằng cụm vị ngữ 「本当にありがたい存在だ」 (thật sự là sự tồn tại đáng trân quý).",`;
const new72 = `にしてみれば,Nにしてみれば,N2,①今何の歌がはやっているかなんて、私にしてみればどうでもいいことだ。それよりもっと大切なことが山ほどある。,個人経営の店主にしてみれば、毎日通ってくれる常連客は本当にありがたい存在だ。,個人経営の店主に,してみれば、,毎日通ってくれる,常連客は,本当にありがたい存在だ。,,Cụm 「個人経営の」 (kinh doanh cá thể) bổ nghĩa cho danh từ 「店主」 (chủ tiệm). Danh từ này kết hợp cấu trúc đứng từ lập trường 「にしてみれば」 (đối với/xét từ góc độ của...) tạo thành vế đầu. Vế sau bắt đầu bằng định ngữ 「毎日通ってくれる」 (lui tới mỗi ngày cho) bổ nghĩa cho chủ ngữ 「常連客は」 (khách quen), kết thúc bằng cụm vị ngữ 「本当にありがたい存在だ」 (thật sự là sự tồn tại đáng trân quý).`;
txt72 = txt72.replace(old72, new72);
fs.writeFileSync(p72, txt72);
console.log('Fixed part_72.csv');

// 3. Fix part_86.csv
const p86 = path.join(BASE_DIR, 'mondai2_ordering/csv_cleaned/set_1_daily/part_86.csv');
let txt86 = fs.readFileSync(p86, 'utf8');
const old86 = `べき,であるべき　A－くあるべき　V－るべき　文語の助動詞「べし」の活用形。現代語の表現では動詞の辞書形に付く。「する」には「するべき」と「すべき」の二つの形が使われる。～べきだ,N3,①学生は勉強す（る）べきだ。,自分の部屋は誰かに頼meas...誰かに頼わず自分で掃除するべきだ,自分の部屋は,誰かに頼meas...,誰かに頼わず,自分で,掃除する,べきだ,`;
const new86 = `べき,であるべき　A－くあるべき　V－るべき　文語の助動詞「べし」の活用形。現代語の表現では動詞の辞書形に付く。「する」には「するべき」と「すべき」の二つの形が使われる。～べきだ,N3,①学生は勉強す（る）べきだ。,自分の部屋は誰かに頼らず自分で掃除するべきだ。,自分の部屋は,誰かに,頼らず,自分で,掃除する,べきだ。,Chủ ngữ 「自分の部屋は」 (phòng của mình) đứng đầu câu. Cụm 「誰かに頼らず」 (không dựa dẫm vào ai) đi kèm với 「自分で」 (tự mình) để bổ nghĩa cho động từ hành động 「掃除する」 (dọn dẹp). Cuối cùng kết hợp với cấu trúc 「べきだ」 (nên/phải) để đưa ra lời khuyên hoặc nghĩa vụ đương nhiên.`;
txt86 = txt86.replace(old86, new86);
fs.writeFileSync(p86, txt86);
console.log('Fixed part_86.csv');

// 4. Fix part_91.csv (multiline)
const p91 = path.join(BASE_DIR, 'mondai2_ordering/csv_cleaned/set_1_daily/part_91.csv');
let txt91 = fs.readFileSync(p91, 'utf8');
const old91 = `までに,Nまでに,N4,①あしたの5時までに連絡してください。,"夕食の時間までに、必ず宿題を終わらせなさい。""「夕食の」 bổ nghĩa cho danh từ thời gian 「時間」. Trợ từ 「までに」 đóng vai trò chỉ thời hạn chót phải thực hiện hành động. Trạng từ 「必ず」 bổ nghĩa cho động từ, và 「宿題を」 làm tân ngữ đứng ngay trước động từ mệnh lệnh 「終わらせなさい」.",時間,までに、,必ず,宿題を,終わらせなさい。,"「夕食の」 bổ nghĩa cho danh từ thời gian 「時間」. Trợ từ 「までに」 đóng vai trò chỉ thời hạn chót phải thực hiện hành động. Trạng từ 「必ず」 bổ nghĩa cho động từ, và 「宿題を」 làm tân ngữ đứng ngay trước động từ mệnh lệnh 「終わらせなさい」."
まま,話しことばでは「まんま」とも言う。～ままだ Nのままだ Naなままだ A一いままま V－たままま,N4,①10年ぶりに会ったが、彼は昔のままだった。,"あの古い部屋は私が子供の時のままだ。",あの古い部屋は`;
const new91 = `までに,Nまでに,N4,①あしたの5時までに連絡してください。,夕食の時間までに、必ず宿題を終わらせなさい。,夕食の,時間までに、,必ず,宿題を,終わらせなさい。,,「夕食の」 bổ nghĩa cho danh từ thời gian 「時間」. Trợ từ 「までに」 đóng vai trò chỉ thời hạn chót phải thực hiện hành động. Trạng từ 「必ず」 bổ nghĩa cho động từ, và 「宿題を」 làm tân ngữ đứng ngay trước động từ mệnh lệnh 「終わらせなさい」。
まま,話しことばでは「まんま」とも言う。～ままだ Nのままだ Naなままだ A一いままま V－たままま,N4,①10年ぶりに会ったが、彼は昔のままだった。,あの古い部屋は私が子供の時のままだ。,あの古い部屋は,私が,子供の,時の,ままだ。,,Chủ ngữ 「あの古い部屋は」 (căn phòng cũ đó) đứng đầu câu. Tiếp theo là chủ ngữ phụ 「私が」 đi với danh từ 「子供」 (trẻ con). Trợ từ 「の」 nối với danh từ 「時」 (lúc/khi). Cuối cùng kết hợp với cấu trúc 「のままだ」 (vẫn giữ nguyên trạng thái như vậy) để kết thúc câu.`;
txt91 = txt91.replace(old91, new91);
fs.writeFileSync(p91, txt91);
console.log('Fixed part_91.csv');

// 5. Fix part_7.csv
const p7 = path.join(BASE_DIR, 'mondai2_ordering/csv_cleaned/set_2_business/part_7.csv');
let txt7 = fs.readFileSync(p7, 'utf8');
const old7 = `いっこうに,いっこうにV－ない,N2,①30分待ったが、彼はいっこうに現れない。,「先方に何度もメールを送っていますが、いっก็ตาม返信が来ない。,「先方に何度もメールを送っていますが、,いっก็ตาม,返信が,来ない。,,,`;
const new7 = `いっこうに,いっこうにV－ない,N2,①30分待ったが、彼はいっこうに現れない。,「先方に何度もメールを送っていますが、いっこうに返信が来ない。」,「先方に何度もメールを送っていますが、,いっこうに,返信が,来ない,。」,,`;
txt7 = txt7.replace(old7, new7);
fs.writeFileSync(p7, txt7);
console.log('Fixed part_7.csv');

// 6. Fix part_10.csv
const p10 = path.join(BASE_DIR, 'mondai2_ordering/csv_cleaned/set_2_business/part_10.csv');
let txt10 = fs.readFileSync(p10, 'utf8');
txt10 = txt10.replace(
  `お～ねがう,おR－ねがう　ごNねがう,N3,①明日うかがいたいと、山田さんにお伝え願えますか。,"本日の会議の資料ですが、こちらの内容でご確認願えますでしょうか。""ごNねがう"" là hình thức khiêm nhường ngữ/lịch sự để nhờ vả đối phương. Với danh động từ ""確認"" (N), ta thêm ""ご"" thành ""ご確認"". Tiếp theo là ""願えます"" (thể khả năng của 願う) kết hợp với đuôi nghi vấn lịch sự ""でしょうか"" để tạo thành mẫu câu nhờ vả trang trọng trong kinh doanh: ""ご確認願えますでしょうか"" (Xin vui lòng xác nhận giúp tôi).""",本日の会議の資料ですが、こちらの内容で,ご確,認,願えます,でしょうか。,"""ごNねがう"" là hình thức khiêm nhường ngữ/lịch sự để nhờ vả đối phương. Với danh động từ ""確認"" (N), ta thêm ""ご"" thành ""ご確認"". Tiếp theo là ""願えます"" (thể khả năng của 願う) kết hợp với đuôi nghi vấn lịch sự ""でしょうか"" để tạo thành mẫu câu nhờ vả trang trọng trong kinh doanh: ""ご確認願えますでしょうか"" (Xin vui lòng xác nhận giúp tôi).""",`,
  `お～ねがう,おR－ねがう　ごNねがう,N3,①明日うかがいたいと、山田さんにお伝え願えますか。,本日の会議の資料ですが、こちらの内容でご確認願えますでしょうか。,本日の会議の資料ですが、こちらの内容で,ご確,認,願えます,でしょうか。,, "ごNねがう" là hình thức khiêm nhường ngữ/lịch sự để nhờ vả đối phương. Với danh động từ "確認" (N), ta thêm "ご" thành "ご確認". Tiếp theo là "願えます" (thể khả năng của 願う) kết hợp với đuôi nghi vấn lịch sự "でしょうか" để tạo thành mẫu câu nhờ vả trang trọng trong kinh doanh: "ご確認願えますでしょうか" (Xin vui lòng xác nhận giúp tôi).`
);
txt10 = txt10.replace(
  `おいそれと（は）～ない,おいそれと（は）V－れない,N1,①子供を産んだばかりの母ネコにはおいそれとは近づけない。,弊社の機密情報に関わるプロジェクトのため、外部の人間にはおいそれとは開示できない。,弊社の機密情報に関わるプロジェクトのため、,,,,,,`,
  `おいそれと（は）～ない,おいそれと（は）V－れない,N1,①子供を産んだばかりの母ネコにはおいそれとは近づけない。,弊社の機密情報に関わるプロジェクトのため、外部の人間にはおいそれとは開示できない。,弊社の機密情報に関わるプロジェクトのため、,外部の,人間には,おいそれとは,開示でき,ない。,Vì đây là dự án liên quan đến thông tin bảo mật của công ty, nên đối với người ngoài thì không thể dễ dàng/tuỳ tiện tiết lộ. Cụm 「外部の人間には」 làm đối tượng, đi kèm cấu trúc 「おいそれとは～ない」 mang nghĩa "không thể dễ dàng làm gì".`
);
txt10 = txt10.replace(
  `おいそれと（は）～ない,おいそれと（は）V－れない,N1,①子供を産んだばかりの母ネコにはおいそれとは近づけない。,"この広いオフィスには、3列おきに高性能な空気清浄機が設置されている。""3列おきに"" nghĩa là cứ cách 3 dãy (hàng ghế). Thứ tự tự nhiên là trạng ngữ chỉ không gian ""この広いオフィスには"" -> danh từ chỉ số lượng + おきに ""3列おきに"" -> cụm chủ vị bổ nghĩa cho đối tượng ""高性能な空気清浄機が設置されている"".""",この広いオフィスには、,3列,おきに,高性能な,空気清浄機が設置されている。,"""3列おきに"" nghĩa là cứ cách 3 dãy (hàng ghế). Thứ tự tự nhiên là trạng ngữ chỉ không gian ""この広いオフィスには"" -> danh từ chỉ số lượng + おきに ""3列おきに"" -> cụm chủ vị bổ nghĩa cho đối tượng ""高性能な空気清浄機が設置されている"".""",`,
  `おきに,数量詞＋おきに,N3,①映画館に入ると、座席は一つおきにしかあいていなかったので、友達とは離れて座ることになった。,この広いオフィスには、3列おきに高性能な空気清浄機が設置されている。,この広いオフィスには、,3列,おきに,高性能な,空気清浄機が設置されている。,, "3列おきに" nghĩa là cứ cách 3 dãy (hàng ghế). Thứ tự tự nhiên là trạng ngữ chỉ không gian "この広いオフィスには" -> danh từ chỉ số lượng + おきに "3列おきに" -> cụm chủ vị bổ nghĩa cho đối tượng "高性能な空気清浄機が設置されている".`
);
txt10 = txt10.replace(
  `おきに,軒おきぐらいに外車を持っている家がある。,N3,①映画館に入ると、座席は一つおきにしかあいていなかったので、友達とは離れて座ることになった。,新工場のラインでは、2台おきに自動検査カメラが配置され、製品をチェックしている。,新工場のラインでは、,,,,,,`,
  `おきに,数量詞＋おきに,N3,①映画館に入ると、座席は一つおきにしかあいていなかったので、友達とは離れて座ることになった。,新工場のラインでは、2台おきに自動検査カメラが配置され、製品をチェックしている。,新工場のラインでは、,2台,おきに,自動検査カメラが,配置され、,製品をチェックしている。,Trạng ngữ chỉ địa điểm 「新工場のラインでは」 đứng đầu. Danh từ chỉ số lượng 「2台」 kết hợp cấu trúc 「おきに」 (cứ cách mỗi...). Tiếp theo là chủ ngữ 「自動検査カメラが」 đi với động từ bị động 「配置され」 (được bố trí), và vế sau diễn tả mục đích 「製品をチェックしている」.`
);
txt10 = txt10.replace(
  `おいて,,N2,①この研究分野の第1人者ということなら、加藤先生をおいてほかはないでしょう。,"担当者の話によれば、今回のシステム障害の原因はおそらくサーバーの過負荷だろう。""おそらく"" (có lẽ/có thể) là phó từ thường đi kèm với các từ phỏng đoán như ""だろう"" ở cuối câu. ""サーバーの"" (của server) bổ nghĩa cho danh từ ""過負荷"" (quá tải). Thứ tự đúng là đặt ""おそらく"" trước thành phần được phỏng đoán ""サーバーの過負荷"" và kết thúc bằng ""だろう"".""",担当者の話によれば、今回のシステム障害の原因は,おそらく,サーバーの,過負荷,だろう。,"""おそらく"" (có lẽ/có thể) là phó từ thường đi kèm với các từ phỏng đoán như ""だろう"" ở cuối câu. ""サーバーの"" (của server) bổ nghĩa cho danh từ ""過負荷"" (quá tải). Thứ tự đúng là đặt ""おそらく"" trước thành phần được phỏng đoán ""サーバーの過負荷"" và kết thúc bằng ""だろう"".""",`,
  `おいて,,N2,①この研究分野の第1人者ということなら、加藤先生をおいてほかはないでしょう。,担当者の話によれば、今回のシステム障害の原因はおそらくサーバーの過負荷だろう。,担当者の話によれば、今回のシステム障害の原因は,おそらく,サーバーの,過負荷,だろう。,, "おそらく" (có lẽ/có thể) là phó từ thường đi kèm với các từ phỏng đoán như "だろう" ở cuối câu. "サーバーの" (của server) bổ nghĩa cho danh từ "過負荷" (quá tải). Thứ tự đúng là đặt "おそらく" trước thành phần được phỏng đoán "サーバーの過負荷" và kết thúc bằng "だろう".`
);
txt10 = txt10.replace(
  `おそれがある,Nのおそれがある V－るおそれがある,N2,①今夜から明日にかけて津波の恐れがあるので、厳重に注意してください。,新規プロジェクトの始動がこれ以上遅れると、今期の目標を達成できないおそれがある。,新規プロジェクトの始動がこれ以上遅れると、,,,,,,`,
  `おそれがある,Nのおそれがある V－るおそれがある,N2,①今夜から明日にかけて津波の恐れがあるので、厳重に注意してください。,新規プロジェクトの始動がこれ以上遅れると、今期の目標を達成できないおそれがある。,新規プロジェクトの始動がこれ以上遅れると、,今期の,目標を,達成できない,おそれが,ある。,Mệnh đề điều kiện 「新規プロジェクトの始動がこれ以上遅れると」 đứng đầu. Danh từ 「今期の」 bổ nghĩa cho tân ngữ 「目標を」. Động từ thể khả năng phủ định 「達成できない」 kết hợp với cấu trúc 「おそれがある」 (e rằng/có nguy cơ) để đưa ra dự báo tiêu cực trong công việc.`
);
txt10 = txt10.replace(
  `おかげで,な／だった　おかげで　Aおかげで　V－たおかげで,N4,①あなたのおかげで助かりました。,"今回の契約書の書式は、前回弊社が提出したものと同じです。""～と同じです"" thể hiện sự giống nhau. ""提出したもの"" (cái đã nộp) đi với trợ từ ""と"" để làm mốc so sánh. Cụm ""前回弊社が"" đóng vai trò định ngữ bổ nghĩa cho ""提出したもの"". Do đó thứ tự là: chủ ngữ -> cụm định ngữ -> từ so sánh + 同じです.""",今回の契約書の書式は、,前回,弊社が,提出したものと,同じです。,"""～と同じです"" thể hiện sự giống nhau. ""提出したもの"" (cái đã nộp) đi với trợ từ ""と"" để làm mốc so sánh. Cụm ""前回弊社が"" đóng vai trò định ngữ bổ nghĩa cho ""提出したもの"". Do đó thứ tự là: chủ ngữ -> cụm định ngữ -> từ so sánh + 同じです.""",`,
  `おかげで,な／だった　おかげで　Aおかげで　V－たおかげで,N4,①あなたのおかげで助かりました。,今回の契約書の書式は、前回弊社が提出したものと同じです。,今回の契約書の書式は、,前回,弊社が,提出したものと,同じです。,, "～と同じです" thể hiện sự giống nhau. "提出したもの" (cái đã nộp) đi với trợ từ "と" để làm mốc so sánh. Cụm "前回弊社が" đóng vai trò định ngữ bổ nghĩa cho "提出したもの". Do đó thứ tự là: chủ ngữ -> cụm định ngữ -> từ so sánh + 同じです.`
);
txt10 = txt10.replace(
  `おなじ,おなじV－る なら／のだったら,N3,①同じ買うなら、少々高くても長持ちするものの方がいい。,同じ新しいシステムを導入するのだったら、社内全体の業務効率化につながるものにしたい。,同じ,,,,,,`,
  `おなじ,おなじV－る なら／のだったら,N3,①同じ買うなら、少々高くても長持ちするものの方がいい。,同じ新しいシステムを導入するのだったら、社内全体の業務効率化につながるものにしたい。,同じ,新しいシステムを,導入する,のだったら、,社内全体の業務効率化に,つながるものにしたい。,Cấu trúc 「同じ～のだったら」 (đằng nào cũng...). Từ 「同じ」 đi cùng động từ 「導入する」 (đưa vào/áp dụng). Vế sau diễn đạt mong muốn 「社内全体の業務効率化につながる」 (dẫn đến tối ưu hoá nghiệp vụ toàn công ty) đi kèm 「ものにしたい」 (muốn biến thành thứ...).`
);
txt10 = txt10.replace(
  `おきに,数量詞＋おきに,N3,①大学行きのバスは10分おきに出ている。,"先週の定例会議で、私がそのような不適切な発言をした覚えはございません。""V-た覚えはない"" nghĩa là ""không nhớ là đã làm việc gì"". Động từ thể quá khứ ""発言をした"" bổ nghĩa cho ""覚えはございません"" (kính ngữ của ない). Tính từ ""不適切な"" bổ nghĩa cho ""発言"", và ""そのような"" bổ nghĩa cho cả cụm ""不適切な発言"".""",先週の定例会議で、私が,そのような,不適切な,発言をした,覚えはございません。,"""V-た覚えはない"" nghĩa là ""không nhớ là đã làm việc gì"". Động từ thể quá khứ ""発言をした"" bổ nghĩa cho ""覚えはございません"" (kính ngữ của ない). Tính từ ""不適切な"" bổ nghĩa cho ""発言"", và ""そのような"" bổ nghĩa cho cả cụm ""不適切な発言"".""",`,
  `覚えはない,V-た覚えはない,N3,①そんなことを言った覚えはない。,先週の定例会議で、私がそのような不適切な発言をした覚えはございません。,先週の定例会議で、私が,そのような,不適切な,発言をした,覚えはございません。,, "V-た覚えはない" nghĩa là "không nhớ là đã làm việc gì". Động từ thể quá khứ "発言をした" bổ nghĩa cho "覚えはございません" (kính ngữ của ない). Tính từ "不適切な" bổ nghĩa cho "発言", và "そのような" bổ nghĩa cho cả cụm "不適切な発言".`
);
txt10 = txt10.replace(
  `おまけに,,N3,①あたりはすっかり暗くなり、おまけに雨まで降ってきた。,新製品はデザインが優れており、おまけに操作も簡単なので顧客から好評だ。,新製品はデザインが優れており、,,,,,,`,
  `おまけに,,N3,①あたりはすっかり暗くなり、おまけに雨まで降ってきた。,新製品はデザインが優れており、おまけに操作も簡単なので顧客から好評だ。,新製品はデザインが優れており、,おまけに,操作も,簡単な,ので,顧客から好評だ。,Vế đầu nêu ưu điểm 「デザインが優れており」. Từ nối 「おまけに」 (thêm vào đó/hơn nữa) bổ sung thêm ưu điểm thứ hai 「操作も簡単な」. Trợ từ chỉ nguyên nhân 「ので」 nối với kết quả đánh giá tích cực 「顧客から好評だ」 (được khách hàng đánh giá cao).`
);
txt10 = txt10.replace(
  `おきに,時間おきに飲んでください。,N3,①この道路には10mおきにポプラが植えられている。,"今回の修正案を提示すれば、先方の担当者も納得してくれると思います。""～と思う"" thể hiện suy nghĩ、 phán đoán của người nói. Trợ từ ""と"" đi sau mệnh đề phán đoán ""先方の担当者も納得してくれる"". ""先方の"" (của phía bên kia) bổ nghĩa cho danh từ ""担当者も"". Thứ tự hợp lý là đưa cụm chủ ngữ vế sau lên trước rồi đến động từ + と思います.""",今回の修正案を提示すれば、,先方の,担当者も,納得してくれると,思います。,"""～と思う"" thể hiện suy nghĩ、 phán đoán của người nói. Trợ từ ""と"" đi sau mệnh đề phán đoán ""先方の担当者も納得してくれる"". ""先方の"" (của phía bên kia) bổ nghĩa cho danh từ ""担当者も"". Thứ tự hợp lý là đưa cụm chủ ngữ vế sau lên trước rồi đến động từ + と思います.""",`,
  `と思う,～と思う,N5,①私は明日雨が降ると思う。,今回の修正案を提示すれば、先方の担当者も納得してくれると思います。,今回の修正案を提示すれば、,先方の,担当者も,納得してくれると,思います。,, "～と思う" thể hiện suy nghĩ, phán đoán của người nói. Trợ từ "と" đi sau mệnh đề phán đoán "先方の担当者も納得してくれる". "先方の" (của phía bên kia) bổ nghĩa cho danh từ "担当者も". Thứ tự hợp lý là đưa cụm chủ ngữ vế sau lên trước rồi đến động từ + と思います.`
);
txt10 = txt10.replace(
  `お思う,～とおもっている,N5,①私は自分のしたことが正しいと思っている。,弊社の開発チームは、来月までにこのバグを修正したいと思っています。,弊社の開発チームは、,,,,,,`,
  `お思う,～とおもっている,N5,①私は自分のしたことが正しいと思っている。,弊社の開発チームは、来月までにこのバグを修正したいと思っています。,弊社の開発チームは、,来月,までに,このバグを,修正したいと,思っています。,Chủ ngữ 「弊社の開発チームは」 đứng đầu. Trạng ngữ thời hạn 「来月までに」 đi kèm tân ngữ 「このバグを」. Động từ thể mong muốn 「修正したい」 kết hợp với cấu trúc 「と思っています」 để trình bày dự định/mong muốn của nhóm phát triển với đối tác/nội bộ.`
);
txt10 = txt10.replace(
  `おきに,軒おきぐらいに外車を持っている家がある。,N3,①映画館に入ると、座席は一つおきにしかあいていなかったので、友達とは離れて座ることになった。,"現在の市場動向を見る限り、我が社の新商品の売り上げはさらに伸びると思われる。""～と思われる"" thể hiện suy nghĩ、 đánh giá mang tính khách quan (nhìn từ góc độ tự nhiên hoặc số liệu). Trợ từ ""と"" đi sau động từ ""伸びる"". ""さらに"" (hơn nữa) là phó từ bổ nghĩa cho ""伸びる"". ""我が社の新商品の売り上げは"" là chủ ngữ của vế phán đoán này.""",現在の市場動向を見る限り、,我が社の,新商品の売り上げは,さらに伸びると,思われる。,"""～と思われる"" thể hiện suy nghĩ、 đánh giá mang tính khách quan (nhìn từ góc độ tự nhiên hoặc số liệu). Trợ từ ""と"" đi sau động từ ""伸びる"". ""さらに"" (hơn nữa) là phó từ bổ nghĩa cho ""伸びる"". ""我が社の新商品の売り上げは"" là chủ ngữ của vế phán đoán này.""",`,
  `と思われる,～と思われる,N3,①この事件は計画的な犯行と思われる。,現在の市場動向を見る限り、我が社の新商品の売り上げはさらに伸びると思われる。,現在の市場動向を見る限り、,我が社の,新商品の売り上げは,さらに伸びると,思われる。,, "～と思われる" thể hiện suy nghĩ, đánh giá mang tính khách quan (nhìn từ góc độ tự nhiên hoặc số liệu). Trợ từ "と" đi sau động từ "伸びる". "さらに" (hơn nữa) là phó từ bổ nghĩa cho "伸びる". "我が社の新商品の売り上げは" là chủ ngữ của vế phán đoán này.`
);
txt10 = txt10.replace(
  `お思う,～とはおもわなかった,N3,①まさか今日あの人が来るとは思わなかった。,入社したばかりの彼が、これほど早く営業成績でトップを取るとは思わなかった。,入社したばかりの彼が、,,,,,,`,
  `お思う,～とはおもわなかった,N3,①まさか今日あの人が来るとは思わなかった。,入社したばかりの彼が、これほど早く営業成績でトップを取るとは思わなかった。,入社したばかりの彼が、,これほど早く,営業成績で,トップを取るとは,思わな,かった。,Chủ ngữ 「入社したばかりの彼が」 gây bất ngờ. Phó từ 「これほど早く」 bổ nghĩa cho cụm hành động 「営業成績でトップを取る」 (đạt top thành tích kinh doanh). Toàn bộ mệnh đề này kết hợp với cấu trúc 「とは思わなかった」 (không ngờ là/không nghĩ là) biểu thị sự ngạc nhiên tột độ.`
);
txt10 = txt10.replace(
  `おそらく,,N3,①おそらく彼はそのことを知っているだろう。,"今後のキャリアプランについて、一度面談のお時間をいただきたいと思っております。""～たいと思っております"" là hình thức khiêm nhường lịch sự của ""たいと思う"" (muốn làm gì). Thể tai của động từ いただく là ""いただきたい"". Tân ngữ của hành động là ""お時間を"" và ""面談の"" bổ nghĩa cho ""お時間を"" (thời gian phỏng vấn).",今後のキャリアプランについて、一度,面談の,お時間を,いただきたいと,思っております。,"""～たいと思っております"" là hình thức khiêm nhường lịch sự của ""たいと思う"" (muốn làm gì). Thể tai của động từ いただく là ""いただきたい"". Tân ngữ của hành động là ""お時間を"" và ""面談の"" bổ nghĩa cho ""お時間を"" (thời gian phỏng vấn).","\n"`,
  `おそらく,,N3,①おそらく彼はそのことを知っているだろう。,今後のキャリアプランについて、一度面談のお時間をいただきたいと思っております。,今後のキャリアプランについて、一度,面談の,お時間を,いただきたいと,思っております。,, "～たいと思っております" là hình thức khiêm nhường lịch sự của "たいと思う" (muốn làm gì). Thể tai của động từ いただく là "いただきたい". Tân ngữ của hành động là "お時間を" và "面談の" bổ nghĩa cho "お時間を" (thời gian phỏng vấn).`
);
fs.writeFileSync(p10, txt10);
console.log('Fixed part_10.csv');
