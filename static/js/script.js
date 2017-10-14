
function valid(form){
	// return false;
	alert("haha");
	var box = document.getElementById("errorMessage");
	var name = form.name;
	var subject = form.subject;
	var message = form.message;
	var empty = [];
	var param = {};
	if (!name.value )
		{empty.push("name")}else{param["name"]=name.value;}
	if (!subject.value)
		{empty.push("subject")}else{param["subject"]=subject.value;}
	if (!message.value)
		{empty.push("message")}else{param["message"]=message.value;}
	console.log(empty);
	alert(empty);
	if (empty.length!==0)
		{box.innerHTML = getString(empty);
			console.log("false");
			alert("false");
			// form.submit(false);
			return false;
		}
	alert("true");
	var url ="/contact?name="+name.value+"&message="+message.value+"&subject="+subject.value;
	form.setAttribute("action",url);
	form.submit(true);
	return true;
	
	// submitForEmail(path)
	// var url = "/contact_us" +"?name="+name.value+"&subject="+subject.value+"&message="+message.value;
	// console.log(url);
	
}
function submit(){
	var box = document.getElementById("errorMessage");
	var name = document.getElementById("name");
	var subject = document.getElementById("subject");
	var message = document.getElementById("message");
	var empty = [];
	var param = {};
	if (!name.value )
		{empty.push("name")}else{param["name"]=name.value;}
	if (!subject.value)
		{empty.push("subject")}else{param["subject"]=subject.value;}
	if (!message.value)
		{empty.push("message")}else{param["message"]=message.value;}
	console.log(empty);
	if (empty.length!==0)
		{box.innerHTML = getString(empty);
			console.log("false")
			return false;
		}
	document.getElementById("form").submit();
	return true;	
}

function submitForEmail(path, parameters){

    var form = $('<form></form>');

    form.attr("method", "post");
    form.attr("action", path);

    $.each(parameters, function(key, value) {
        var field = $('<input></input>');

        field.attr("type", "hidden");
        field.attr("name", key);
        field.attr("value", value);

        form.append(field);
    });

    // The form needs to be a part of the document in
    // order for us to be able to submit it.
    $(document.body).append(form);
    form.submit();

}
function getString(list){
	var result = "field ";
	for(var i in list){
		result+=list[i];
		result+=" "
	}
	result+="is missing."
	return result;
}

function comment(id){
	var commentstring = window.localStorage.getItem('comments'+id);
	// console.log(comments.length)

	if(!commentstring ){
		console.log(commentstring)
		var comments=[];
	}else{
		var comments = JSON.parse(commentstring)
	}
	var name = document.getElementById("comment_name");
	var message = document.getElementById("comment_message");
	if(name.value&& message.value){
		comments.push({"name":name.value,"message":message.value});
	}
	// console.log(comments.length)
	window.localStorage.setItem('comments'+id,JSON.stringify(comments));

	showcomment(id);
}
// showcomment();
function showcomment(id){
	var commentstring = window.localStorage.getItem('comments'+id);
	if(!commentstring){ var comments=[];}else{
		var comments=JSON.parse(commentstring);
	}
	var table = document.getElementById("comment_table");
	if(!table){
		console.log("no table")
		return;}
	var tableRows = table.rows;
	var rowCount = tableRows.length;

	for (var x=rowCount-1; x>=0; x--) {
	   table.deleteRow(x);
	}
	if(comments.length>0){
	var newRow = document.createElement("tr");
	var name = document.createElement("td");
	var message = document.createElement("td");
	name.innerHTML = "name";
	message.innerHTML ="message";
	newRow.appendChild(name);
	newRow.appendChild(message);
	table.appendChild(newRow);

	}
	for(var i in comments){
		console.log(i);
	var newRow = document.createElement("tr");
	var name = document.createElement("td");
	var message = document.createElement("td");
	name.innerHTML = comments[i]["name"];
	message.innerHTML = comments[i]["message"];
	newRow.appendChild(name);
	newRow.appendChild(message);
	table.appendChild(newRow);
	}

}
