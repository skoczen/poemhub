$(function(){
    // Yes, I know this is circa-2008 style. I had no internet for a week when I wrote it and only jquery to write with.
    // Suck it. :)

    window.Poemr = window.Poemr || {};
    Poemr.poem = {};
    Poemr.poem.editor = {};
    Poemr.poem.actions = {};
    Poemr.poem.state = {};
    Poemr.poem.editor.editing_nodes = [];
    Poemr.poem.editor.is_editing = false;
    Poemr.poem.state.title = "";
    Poemr.poem.state.body = "";

    // Fantastic button is totally fake. For now.
    $(".fantastic_button").click(function(){
        $(this).toggleClass("clicked");
    });

    Poemr.poem.editor.start_editing = function() {
        $(".edit_bar").addClass("editing");
        $(".poem").addClass("editing");
        Poemr.poem.editor.add_nicedit_editors();
        return false;
    };
    Poemr.poem.editor.add_nicedit_editors = function() {
        $(".editable").each(function(){
            id = $(this).attr("id");
            ed = new nicEditor({
                fullPanel : false,
                buttonList : ['bold','italic','underline','left','center','right']
            }).panelInstance(id, {hasPanel : true});
            Poemr.poem.editor.editing_nodes[id] = ed;
        });
        $(".title .nicEdit-main").focus();
    };
    Poemr.poem.editor.cancel_editing = function() {
        $(".edit_bar").removeClass("editing");
        $(".poem").removeClass("editing");
        Poemr.poem.editor.remove_nicedit_editors();
        return false;
    };
    Poemr.poem.editor.remove_nicedit_editors = function() {
        $(".editable").each(function(){
            id = $(this).attr("id");
            editor = Poemr.poem.editor.editing_nodes[id];
            var new_html = nicEditors.findEditor(id).getContent();
            editor.removeInstance(id);
            editor = null;
            $(this).html(new_html);
        });
    };

    Poemr.poem.actions.save_revision = function() {
        if (Poemr.poem.state.title != nicEditors.findEditor("poem_title").getContent() ||
            Poemr.poem.state.body != nicEditors.findEditor("poem_body").getContent()) {
            $.ajax({
                url: Poemr.urls.save_revision,
                type: "post",
                dataType: "json",
                data: {
                    "title": nicEditors.findEditor("poem_title").getContent(),
                    "body": nicEditors.findEditor("poem_body").getContent(),
                },
                params: {
                    'csrf_token': Poemr.tokens.csrf,
                    'csrf_name': 'csrfmiddlewaretoken',
                    'csrf_xname': 'X-CSRFToken',
                },
                success: function(json){
                    alert("saved!");
                    Poemr.poem.state.title = nicEditors.findEditor("poem_title").getContent();
                    Poemr.poem.state.body = nicEditors.findEditor("poem_body").getContent();
                }
            });
        }
    };
    Poemr.poem.actions.init = function() {
        Poemr.poem.state.title = $("#poem_title").html();
        Poemr.poem.state.body = $("#poem_body").html();

        // Handlers
        $(".save_revision_button").click(Poemr.poem.actions.save_revision);
        $(".start_editing_button").click(Poemr.poem.editor.start_editing);
        $(".cancel_editing_button").click(Poemr.poem.editor.cancel_editing);

        bkLib.onDomLoaded(nicEditors.allTextAreas);
    };
    Poemr.poem.actions.init();

});
