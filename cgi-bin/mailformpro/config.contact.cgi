## サンクスページのURL(URLかsend.cgiから見た相対パス)
$config{'ThanksPage'} = '../../contact_thanks.html';

## 設置者に届くメールの件名
$config{'subject'} = '[ %s ] お問い合せフォームから';

## 設置者に届くメールの本文整形
$_TEXT{'posted'} = <<'__posted_body__';
<_mfp_date_>
お問い合せフォームより以下のメッセージを受け付けました。
──────────────────────────
受付番号：<_mfp_serial_>

<_resbody_>

──────────────────────────
　MOVIE STAR RECORDS
　http://movie-star-records.info/
　staff@movie-star-records.info
━━━━━━━━━━━━━━━━━━━━━━━━━━
__posted_body__

## ※※※！！！※※※！！！※※※！！！※※※！！！※※※！！！※※※
## 自動返信メールの件名 (有効にする場合は下記の行頭#を外してください。)
## ※※※！！！※※※！！！※※※！！！※※※！！！※※※！！！※※※

$config{"ReturnSubject"} = '[ %s ] お問い合せありがとうございました！';

## 自動返信メールの本文
$_TEXT{'responder'} = <<'__return_body__';
<_contact_name_> 様
──────────────────────────

お問合せいただき、ありがとうございました。
内容を確認させていただき、後ほど改めて、
ご連絡させていただきます。

─お問合せ内容の確認─────────────────
受付番号：<_mfp_serial_>
<_resbody_>
──────────────────────────

このメールに心当たりの無い場合は、お手数ですが
下記連絡先までお問い合わせください。

━━━━━━━━━━━━━━━━━━━━━━━━━━
　MOVIE STAR RECORDS
　http://movie-star-records.info/
　staff@movie-star-records.info
━━━━━━━━━━━━━━━━━━━━━━━━━━
__return_body__

## 各種データを格納しているファイル

$config{'data.dir'} = './data.contact/';

## [0] Serial, [1] InputTime, [2] ConfirmTime, [3] UniqueUser
$config{'file.data'} = "$config{'data.dir'}dat.mailformpro.cgi";

## ドロップ検知
$config{'file.drop'} = "$config{'data.dir'}dat.drop.cgi";

## jsキャッシュ
$config{'file.cache'} = "$config{'data.dir'}mfp.cache.js";

## Prefix
$config{'prefix'} = '_MFP_CONTACT';

1;