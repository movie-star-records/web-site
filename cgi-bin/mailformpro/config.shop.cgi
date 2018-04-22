## サンクスページのURL(URLかsend.cgiから見た相対パス)
$config{'ThanksPage'} = '../../shop_thanks.html';

## 設置者に届くメールの件名
$config{'subject'} = '[ %s ] ご注文フォームから';

## 設置者に届くメールの本文整形
$_TEXT{'posted'} = <<'__posted_body__';
<_mfp_date_>
ご注文フォームより以下のご注文を受け付けました。
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

$config{"ReturnSubject"} = '[ %s ] ご注文ありがとうございました！';

## 自動返信メールの本文
$_TEXT{'responder'} = <<'__return_body__';
<_contact_name_> 様
──────────────────────────

ご注文いただき、ありがとうございました。
内容を確認させていただき、後ほど改めて、
ご連絡させていただきます。

─ご注文内容の確認─────────────────
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

$config{'data.dir'} = './data.shop/';

## [0] Serial, [1] InputTime, [2] ConfirmTime, [3] UniqueUser
$config{'file.data'} = "$config{'data.dir'}dat.mailformpro.cgi";

## ドロップ検知
$config{'file.drop'} = "$config{'data.dir'}dat.drop.cgi";

## jsキャッシュ
$config{'file.cache'} = "$config{'data.dir'}mfp.cache.js";

## Prefix
$config{'prefix'} = '_MFP_SHOP';

1;