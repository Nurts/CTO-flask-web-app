function show(hide){
    if(hide != 1){
        var hash_block  = document.getElementById("hash-block");
        hash_block.style.visibility = "visible"
        var content_block = document.getElementById("content-block");
        content_block.style.height = "500px"

        if(hide == 2){
            var not_exist_block = document.getElementById("status-icon-2");
            not_exist_block.style.visibility = "visible";
            var status_label = document.getElementById("status-label");
            status_label.innerHTML = "Нет ID"
            var hash_code_block = document.getElementsByClassName("hash-code-block")[0];
            hash_code_block.style.visibility = "hidden";
            content_block.style.height = "400px"
            return false
        }
        return true;
    }
    return false;
}

function main(status, hide){
    if(show(hide)){
        var hashes = document.getElementsByClassName("hash-hover");
        var first_twos = document.getElementsByClassName("first-two-chars");
        var last_twos = document.getElementsByClassName("last-two-chars");
        var random_colors = document.getElementsByClassName("random-colors");
        var i;
        var equal = true;
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
                    let box = document.createElement("div");
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
        
        var status_label = document.getElementById("status-label");
        var status_icon = document.getElementById("status-icon-1");
        
        if(hashes.length > 0 && !equal){
            status_label.innerHTML = "Введенные данные некорректны"
        }
        else if(hashes.length > 0 && equal){
            if(status == "OK"){
                status_label.innerHTML = "Законапослушный автоводитель. Нарушений не имеется"
                status_icon.src = "/static/images/small_checked.png"
            }
            else{
                status_label.innerHTML = "Автоводитель имеет нарушения"
            }
        }
    }
}

