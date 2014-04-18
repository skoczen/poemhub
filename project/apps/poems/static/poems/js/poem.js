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
    var ed;

    // Fantastic button is totally fake. For now.
    $(".fantastic_button").click(function(){
        $(this).toggleClass("clicked");
    });

    Poemr.poem.editor.toggle_options = function() {
        $(".poem_form").toggleClass("show_options");
        return false;
    };

    Poemr.poem.editor.start_editing = function() {
        $(".edit_bar").addClass("editing");
        $(".poem").addClass("editing");
        $(".poem_form").addClass("editing");
        // $(".revisions_button").hide();
        Poemr.poem.editor.add_nicedit_editors();
        return false;
    };
    Poemr.poem.editor.add_nicedit_editors = function() {
        Poemr.poem.editor.editing_node = new nicEditor({
                fullPanel : false,
                buttonList : ['bold','italic','underline']
                // Currently broke as fuck.  ,'left','center','right'
        }).panelInstance("edit_pane", {hasPanel: true});
        $(".poem .editable").each(function(){
            id = $(this).attr("id");
            Poemr.poem.editor.editing_node.addInstance(id, {hasPanel : true});
            Poemr.poem.editor.editing_nodes[id] = ed;
        });
        $(".title .nicEdit-main").focus();
    };
    Poemr.poem.editor.cancel_editing = function() {
        $(".edit_bar").removeClass("editing");
        $(".poem").removeClass("editing");
        $(".poem_form").removeClass("editing");
        $(".poem_form").removeClass("show_options");
        // $(".revisions_button").show();
        Poemr.poem.editor.remove_nicedit_editors();
        return false;
    };
    Poemr.poem.editor.remove_nicedit_editors = function() {
        $(".poem .editable").each(function(){
            id = $(this).attr("id");
            var new_html = nicEditors.findEditor(id).getContent();
            $(this).html(new_html);
        });
        Poemr.poem.editor.editing_node.removeInstance("edit_pane");
        Poemr.poem.editor.editing_node = null;
    };

    Poemr.poem.actions.init = function() {

        $(".poem_form").ajaxForm({
            beforeSerialize: function() {
                $("#id_title").val(nicEditors.findEditor("poem_title").getContent());
                $("#id_body").val(nicEditors.findEditor("poem_body").getContent());
            },
            success: function(json) {
                // alert("saved!");
                console.log(json);
                Poemr.poem.editor.cancel_editing();
                if (json.new_url) {
                    document.location = json.new_url;
                }
            }
        });
        // Handlers
        // $(".save_revision_button").click(Poemr.poem.actions.save_revision);
        $(".publish_button").click(function(){
            if (confirm("This will make your piece available to the general public.  There's no undo, but it is pretty awesome.  Ready to go?")) {
                $("#id_is_draft").val("False");
                $(".poem_form").submit();
            }
            return false;
        });
        $(".start_editing_button").click(Poemr.poem.editor.start_editing);
        $(".cancel_editing_button").click(Poemr.poem.editor.cancel_editing);
        $(".options_button").click(Poemr.poem.editor.toggle_options);

        bkLib.onDomLoaded(nicEditors.allTextAreas);
    };
    Poemr.poem.actions.init();

});
