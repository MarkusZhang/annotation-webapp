window.addEventListener('keydown',this.check,false);
KEY_YES = 97;
KEY_NO = 98;
KEY_ENTER = 13;
YES_RETURN_VALUE = 1;
NO_RETURN_VALUE = -1;


function show_yes_img(){
    $("#no_img").addClass("hidden");
    $("#yes_img").removeClass("hidden");
}

function show_no_img(){
    $("#yes_img").addClass("hidden");
    $("#no_img").removeClass("hidden");
}

function conv_arr_to_str(arr){
    return_str = "";
    for (i=0;i<arr.length-1;i++){
        return_str += arr[i] + ","
    }
    return_str += arr[arr.length-1];
    return return_str;
}

function check(e) {
    keyCode = e.keyCode;
    if (keyCode == KEY_YES){
        $("#yes_selection").prop("checked", true);
        show_yes_img();
    }
    else if (keyCode == KEY_NO){
        $("#no_selection").prop("checked", true);
        show_no_img();
    }
    else if (keyCode == KEY_ENTER){
        // check whether radio box is checked
        yes_selected = $("#yes_selection").prop("checked");
        no_selected = $("#no_selection").prop("checked");
        choice = null;
        if (!yes_selected && !no_selected){
            alert("Please select yes or no!");
            return;
        }
        else if (yes_selected){
            choice = YES_RETURN_VALUE;
        }
        else{  // no selected
            choice = NO_RETURN_VALUE;
        }

        // record choice
        choices.push(choice);

        if (current_img_index == NUM_IMAGES){
            // submit the results
            query_string = "product_name=" + PRODUCT_NAME + "&annotations=" + conv_arr_to_str(choices);
            window.location.href = "/submit_annotation?" + query_string;
        }
        else{
            // show the next image
            cur_img_id = "customer_img_" + current_img_index;
            current_img_index += 1;
            next_img_id = "customer_img_" + current_img_index;
            $("#" + cur_img_id).addClass("hidden");
            $("#" + next_img_id).removeClass("hidden");
            $("#index_span").text(current_img_index + "/" + NUM_IMAGES);
            // clear selection
            $("#no_selection").prop("checked", false);
            $("#yes_selection").prop("checked", false);
            $("#yes_img").addClass("hidden");
            $("#no_img").addClass("hidden");
        }
    }
}