$(function() { // onload function -load시
    $('#comment_create_btn').on('click',function(){
        $.ajax({
            async:true, //비동기 방식으로 호출
            url : '/bbs/commentCreate/',
            type: 'GET',
            data:{
                board_id : $('#board_id').text(),
                user_name : $('#c_name').val(),
                user_content : $('#c_content').val(),
            },
            dataType : 'json', //요청 후 서버로 받을 데이터 형식
            success: function(result){  //성공시
                let tr = $("<tr></tr>")
                let author_td = $("<td></td>").text(result.comment_author)
                let content_td = $("<td></td>").text(result.comment_content)
                let delete_td = $("<td></td>").text('삭제')
                tr.append(author_td)
                tr.append(content_td)
                tr.append(delete_td)

                $('tbody').prepend(tr)
            },
            error:function(){
                alert('Error!')    
            }
        })
    })
})