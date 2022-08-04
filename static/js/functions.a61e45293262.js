
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

function showhide(object){
    if (object.hidden == false){
        object.hidden = true
    }       
    else{
        object.hidden = false
    }
           
}


/*fetchpage(url que deve ser passada, dados em formato dict {info:resposta}, objeto)
Utilize a snake_case notation ou upperCase. 
Essa funÃ§Ã£o Ã© sincrona, para receber o valor prometido em ret,
devemos chamar uma funÃ§Ã£o asyncrona para entÃ£o chamar o fetchobject */
function fetchobject(url,data,object){
   
    const ret = fetchpage(url,data).then(ret =>object.innerHTML = ret)
    
    return(ret)
}

/*
fetchpage(url que deve ser passada, dados em formato dict {info:resposta})
retorno Ã© uma pagina de forma asyncrona. logo se tentar chamar a resposta irÃ¡ receber um [object promise]
Para receber um objeto, deve chamar a funÃ§Ã£o fetchobject passando a utl, os dados e o nome do objeto que deseja passar.
O nome dos objetos nÃ£o pode ser separado por '.' ou por '-' pois isso segrega o nome durante o cÃ³digo.
Utilize a snake_case notation ou upperCase.*/
async function fetchpage(url,data){

    data = JSON.stringify(data)

    var csrftoken = getCookie('csrftoken');
    var headers = new Headers();
    headers.append('X-CSRFToken', csrftoken);
	headers.append('Accept', 'application/json');
    headers.append('X-Requested-With', 'XMLHttpRequest');
    

    //FETCH -> IrÃ¡ atualizar o banco de dados do checkbo com base no valor do checkbox.
    //let url =  // URL
    
    let response = await fetch(url,{
        method: 'POST',
        credentials: 'include',     
        headers: headers,
        body: JSON.stringify(data)
      });
    

       //FETCH ASYNCRONO - Lembrando que a funÃ§Ã£o precisa ser asyncrona.
    obj = await response.text()
    
    
    return (obj) 
}

async function fetchpage2(url,data){


    var csrftoken = getCookie('csrftoken');
    var headers = new Headers();
    headers.append('X-CSRFToken', csrftoken);
	headers.append('Accept', 'application/json');
    headers.append('X-Requested-With', 'XMLHttpRequest');
    

    //FETCH -> IrÃ¡ atualizar o banco de dados do checkbo com base no valor do checkbox.
    //let url =  // URL
    
    let response = await fetch(url,{
        method: 'POST',
        credentials: 'include',     
        headers: headers,
        body: data
      });
    

       //FETCH ASYNCRONO - Lembrando que a funÃ§Ã£o precisa ser asyncrona.
    obj = await response.text()
    
    
    return (obj) 
}

/*getobject Ã© semelhante ao fetchobject mas aqui utilizamos o mÃ©todo GET */
function getobject(url,object){
   
    const ret = getpage(url).then(ret =>object.innerHTML = ret)
    
    return(ret)
}

/*getpage Ã© simular ao fetchpage, mas aqui nÃ³s utilizamos o mÃ©todo get */
async function getpage(url){

    
    let response = await fetch(url,{
        method: 'GET',
        credentials: 'include'

      });
    
       //FETCH ASYNCRONO - Lembrando que a funÃ§Ã£o precisa ser asyncrona.
    obj = await response.text()
    
    
    return (obj) 
}




function switchhidden(item1,item2){
    if(item1.hidden == false){
        item1.hidden = true
        item2.hidden = false
    }
    else {
        item1.hidden = false
        item2.hidden = true
    }

}

function switchchildren(object){
	switchhidden(object.children[0],object.children[1])
}

//Confirma uma aÃ§Ã£o e devolve todo o html para a pÃ¡gina.
function confirmation(url,data, message="Deseja mesmo fazer isso"){
    if (confirm(message)){

        const ret = fetchpage(url,data).then(ret =>document.body.innerHTML = ret)
    } 
    else{
        
        return 0
    }
}

function uncheck(object){
    object.checked = false
}    

function createData(key,form){
formdata = {}
for (let index = 0; index < form.length; index++) {
	if (form[index].disabled == false)
  formdata[form[index].id] = form[index].value
    
}
    formdata['key'] = key
    return(formdata)
}

function createDataFiles(key,form){
var formdata = new FormData()
for (let index = 0; index < form.length; index++) {
	if (form[index].disabled == false){
		if (form[index].type == 'file')
		{
			formdata.append(form[index].id, form[index].files[0])
		} else {
			
		formdata.append(form[index].id, form[index].value)
		
		}
	}
    
}
    formdata.append('key', key)
    return(formdata)
}

const random = (length = 8) => {
    // Declare all characters
    let chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';

    // Pick characers randomly
    let str = '';
    for (let i = 0; i < length; i++) {
        str += chars.charAt(Math.floor(Math.random() * chars.length));
    }

    return str;

};


//Permite que um elemento seja re-posicionado para dentro de outro.
function impersonate(objeto,body, remove=true){
    objeto.innerHTML = body.innerHTML
    if (remove == true)
	body.remove()
}

function checkfile(sender) {
    var validExts = sender.accept.split(',');
    var fileExt = sender.value;
    fileExt = fileExt.substring(fileExt.lastIndexOf('.'));
    if (validExts.indexOf(fileExt) < 0) {
      alert("Invalid file selected, valid files are of " +
               validExts.toString() + " types.");
			   sender.value = ''
      return false;
    }
    else return true;
}

function slugify(text)
{
    return text.toLowerCase().replace(/ /g,'-').replace(/[^\w-]+/g,'');
}

function reload(time){
    reloadtime = function semireload(){
        location.reload()
    }
    setTimeout(reloadtime,time)
}