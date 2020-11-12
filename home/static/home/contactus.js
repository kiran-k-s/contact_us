function nameValidate()
{
var name=document.getElementById("inputName").value;

if(name.length>=3 && name.length <=100)
		{
			if(/^[a-zA-Z\s]+$/.test(name))
			{
                document.getElementById("nameError").innerHTML ="";
				return true;
			}
		else
			{
                document.getElementById("nameError").innerHTML ="Error: Name should only contain characters and space.";
				return false;
			}
		}
		
else
    {	
        document.getElementById("nameError").innerHTML ="Error: Name length should be greater than 3 characters and less than 100 characters";
        return false;
    }		
}

function mailValidate()
{
var email=document.getElementById("inputEmail").value;
const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
if(re.test(email))
		{
			document.getElementById("mailError").innerHTML ="";
			return true;
		}
    
else
		{
			document.getElementById("mailError").innerHTML ="Error: Invalid E-mail id";
			return false;
		}

}

function numberValidate()
{

	var  mobile=document.getElementById("inputPhone").value;
	const re=/^\d+$/;

	if(re.test(mobile)|| mobile.length ==0) 
		{
		if(mobile.length==0 || mobile.length ==10)
			{
			document.getElementById("phoneError").innerHTML ="";
			return true;
			}
		else
			{
			document.getElementById("phoneError").innerHTML ="Error: Invalid phone number";
			return false;
			}
		}
	else
		{
			document.getElementById("phoneError").innerHTML ="Error: Invalid phone number";
			return false;
		}

}

function descriptionValidate()
{
	var  description=document.getElementById("inputDescription").value;

	if(description.length>=20)
		{
		document.getElementById("descriptionError").innerHTML ="";
		return true;
		}
	else
		{
		document.getElementById("descriptionError").innerHTML ="Error: Description is mandatory with a minimum of 20 character length";
		return false;
		}
	
}


/*function getCookie(name) { 
    var cookieValue = null; 
    if (document.cookie && document.cookie != '') { 
        var cookies = document.cookie.split(';'); 
        for (var i = 0; i < cookies.length; i++) { 
            var cookie = jQuery.trim(cookies[i]); 
            if (cookie.substring(0, name.length + 1) == (name + '=')) { 
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1)); break; 
            } 
        } }}
    */

/*   $(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

   function getCookie(c_name)
   {
	   if (document.cookie.length > 0)
	   {
		   c_start = document.cookie.indexOf(c_name + "=");
		   if (c_start != -1)
		   {
			   c_start = c_start + c_name.length + 1;
			   c_end = document.cookie.indexOf(";", c_start);
			   if (c_end == -1) c_end = document.cookie.length;
			   return unescape(document.cookie.substring(c_start,c_end));
		   }
	   }
	   return "";
	}*/
        

//function insertOne()
//{

   // console.log("Hello");
	//var nameok=nameValidate();
	//var emailok=mailValidate();
	//var mobok=numberValidate();
	//var desok=descriptionValidate();
	
    
	//if(nameok==true && emailok==true && mobok==true && desok==true)
	//{


        $(document).ready(function(){
            $('#fbutton').click(function(e){
                  //var isvalid=validation()
                  
                  e.preventDefault();
                  console.log("Hello");
                    var nameok=nameValidate();
                    var emailok=mailValidate();
                    var mobok=numberValidate();
                    var desok=descriptionValidate();
          if(nameok==true && emailok==true && mobok==true && desok==true){
                  $.ajax({

                    headers: { "X-CSRFToken": "{{ csrf_token }}" },

                          method:'POST',
                          url:'/add',
                          data:{
                                'csrfmiddlewaretoken':'{{ csrf_token }}',

                                name:$('#inputName').val(),
                                email:$('#inputEmail').val(),
                                phone:$('#inputPhone').val(),
                                description:$('#inputDescription').val(),
                         },
                      
                    success:function(response){
                     
                      document.getElementById('success').innerHTML="Succesfully added data"
                     
                      $('#cform').trigger('reset')
                    

                    }
                  

                })

          }


                })          
        });
    
		
		
	//}
//}
