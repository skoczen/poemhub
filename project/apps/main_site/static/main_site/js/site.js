$(function(){
    // Todo: you know, real code.
    var editing_nodes = [];
    $(".fantastic_button").click(function(){
        $(this).toggleClass("clicked");
    });
    $(".toggle_editing_button, .save_draft_button").click(function(){
        $(".edit_bar").toggleClass("editing");
        $(".poem").toggleClass("editing");
        if ($(".edit_bar").hasClass("editing")) {
            $(".editable").each(function(){
                id = $(this).attr("id");
                ed = new nicEditor({
                    fullPanel : false,
                    buttonList : ['bold','italic','underline','left','center','right']
                }).panelInstance(id, {hasPanel : true});
                editing_nodes[id] = ed;
            });
            return false;
        } else {
            $(".editable").each(function(){
                id = $(this).attr("id");
                editor = editing_nodes[id];
                var new_html = nicEditors.findEditor(id).getContent();
                editor.removeInstance(id);
                editor = null;
                $(this).html(new_html);
            });
            return false;
        }
    });
    $(".home_buttons .button.readers").click(function(){
        // Maaaan this brings me back to 2006-style.
        $(".home_buttons .button").removeClass("current");
        $(this).addClass("current");
        $(".detail_section").hide();
        $(".detail_section.for_readers").show();
        return false;
    });
    $(".home_buttons .button.writers").click(function(){
        $(".home_buttons .button").removeClass("current");
        $(this).addClass("current");
        $(".detail_section").hide();
        $(".detail_section.for_writers").show();
        return false;
    });
});
