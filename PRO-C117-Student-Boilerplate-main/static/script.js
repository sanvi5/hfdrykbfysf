$(document).ready(function(){

    console.log('Ready')

   
    $('#submit_button_id').click(function(){ 

        
        let text_value = $('#text_area_id').val() 

        
        let input_text = {'customer_review': text_value} 

        // ajax request
        $.ajax({

            // type of web request
            type : 'POST', 


            data : JSON.stringify(input_text), 
            
            dataType : 'json',

            // contentType
            contentType : 'application/json',

            // if everything is successful, run this function
            success : function(result){
                // extract prediction and emoticon url from result
                let sentiment = result.sentiment;
                let image_path = result.image_path;

            },

            
            error : function(result){
                console.log(result);
            }
        })

       
        $('#text_area_id').val("");
    })
        
})
