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
        };
    });
});
