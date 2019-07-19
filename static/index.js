function show(hide){
    console.log(hide)
    if(hide == 0){
        var hash_block  = document.getElementById("hash-block");
        hash_block.style.visibility = "visible"
        var content_block = document.getElementById("content-block");
        content_block.style.height = "600px"
    }
    else if(hide == 2){
        var not_exist_block = document.getElementById("not-exist-block");
        not_exist_block.style.visibility = "visible";
    }
}

function main(){

    var hashes = document.getElementsByClassName("hash-hover");
    var status = document.getElementsByClassName("status");
    var first_twos = document.getElementsByClassName("first-two-chars");
    var last_twos = document.getElementsByClassName("last-two-chars");
    var status_text = document.getElementsByClassName("status-text");
    var random_colors = document.getElementsByClassName("random-colors");
    var i;
    var equal = true, isempty = false;
    for(i = 0; i < hashes.length; i++ ){
        var hash = hashes[i].innerHTML;
        var first_hash = hashes[0].innerHTML;

        if(hash !== first_hash){
            equal = false;
        }

        if(hash.length > 4 && i < first_twos.length && i < last_twos.length && i < random_colors.length){
            
            first_twos[i].innerHTML = hash.substring(0, 2);
            
            
            let color_l = 2, color_r = 8;
            
            while(color_r <= hash.length){
                var box = document.createElement("div");
                box.style.width = "1ch";
                box.style.height = "9pt";
                box.style.backgroundColor = "#" + hash.substring(color_l, color_r);
                box.style.display = "inline-block";
                random_colors[i].appendChild(box);
                color_l += 6;
                color_r += 6;
            }

            last_twos[i].innerHTML = hash.substring(color_l, hash.length);
        }
    }
    
    if(hashes.length > 0 && hashes[0].innerHTML != "0" && equal){
        for(i = 0; i < status.length; i++){
            status[i].style.backgroundColor = "#91ff87";
            if(i < status_text.length){
                status_text[i].innerHTML = "OK";
            }
        }
    }
    else if(hashes.length > 0 && !equal){
        for(i = 0; i < status.length; i++){
            status[i].style.backgroundColor = "#f76d6d";
            if(i < status_text.length){
                status_text[i].innerHTML = "NOT OK";
            }
        }
    }

}

