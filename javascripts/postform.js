function validateFormContact{
$('#postForm').attr('action','cgi-bin/mailformpro/mailformpro.cgi?type=contact');
return true;
};

function validateFormShop{
$('#postForm').attr('action','cgi-bin/mailformpro/mailformpro.cgi?type=shop');
return true;
};