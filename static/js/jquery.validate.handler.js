$(function(){
  $("#form").validate({
    rules : {
      itemName: {
        required: true,
      },
      amount: {
        required: true,
        number: true,
      },
      storeId: {
        number: true,
      },
    },
    messages: {
      itemName: {
        required: "商品名を入力してください",
      },
      amount: {
        required: "金額を入力してください",
        number: "数値のみを入力してください",
      },
      storeId: {
        number: "数値のみを入力してください",
      },
    },
  })
})