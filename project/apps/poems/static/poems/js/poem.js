$(function(){
    // Yes, I know this is circa-2008 style. I had no internet for a week when I wrote it and only jquery to write with.
    // Suck it. :)

    window.Poemhub = window.Poemhub || {};
    Poemhub.poem = {};
    Poemhub.poem.editor = {};
    Poemhub.poem.actions = {};
    Poemhub.poem.state = {};
    Poemhub.poem.editor.editing_nodes = [];
    Poemhub.poem.editor.is_editing = false;
    Poemhub.poem.state.title = "";
    Poemhub.poem.state.body = "";
    var ed;

    Poemhub.poem.editor.toggle_options = function() {
        $(".poem_form").toggleClass("show_options");
        return false;
    };

    Poemhub.poem.editor.start_editing = function() {
        $(".edit_bar").addClass("editing");
        $(".poem").addClass("editing");
        $(".poem_form").addClass("editing");
        // $(".revisions_button").hide();
        Poemhub.poem.editor.add_nicedit_editors();
        return false;
    };
    Poemhub.poem.editor.add_nicedit_editors = function() {
        Poemhub.poem.editor.editing_node = new nicEditor({
                fullPanel : false,
                buttonList : ['bold','italic','underline']
                // Currently broke as fuck.  ,'left','center','right'
        }).panelInstance("edit_pane", {hasPanel: true});
        $(".poem .editable").each(function(){
            id = $(this).attr("id");
            Poemhub.poem.editor.editing_node.addInstance(id, {hasPanel : true});
            Poemhub.poem.editor.editing_nodes[id] = ed;
        });
        $(".title .nicEdit-main").focus();
    };
    Poemhub.poem.editor.cancel_editing = function() {
        $(".edit_bar").removeClass("editing");
        $(".poem").removeClass("editing");
        $(".poem_form").removeClass("editing");
        $(".poem_form").removeClass("show_options");
        // $(".revisions_button").show();
        Poemhub.poem.editor.remove_nicedit_editors();
        return false;
    };
    Poemhub.poem.editor.remove_nicedit_editors = function() {
        $(".poem .editable").each(function(){
            id = $(this).attr("id");
            var new_html = nicEditors.findEditor(id).getContent();
            $(this).html(new_html);
        });
        Poemhub.poem.editor.editing_node.removeInstance("edit_pane");
        Poemhub.poem.editor.editing_node = null;
    };
    Poemhub.poem.toggle_fantastic = function() {
        $(this).toggleClass("clicked");
        $.ajax({
            url: Poemhub.urls.fantastic,
            data: {
                "on": $(this).hasClass("clicked")
            },
            success: function(json) {
                $(".fantastic_button .num_agree").html(json.num_people).addClass("visible");
            }
        });
    };

    Poemhub.poem.actions.init = function() {

        $(".poem_form").ajaxForm({
            beforeSerialize: function() {
                $("#id_title").val(nicEditors.findEditor("poem_title").getContent());
                $("#id_body").val(nicEditors.findEditor("poem_body").getContent());
            },
            success: function(json) {
                Poemhub.poem.editor.cancel_editing();
                if (json.new_url) {
                    document.location = json.new_url;
                }
            }
        });
        // Handlers
        // $(".save_revision_button").click(Poemhub.poem.actions.save_revision);
        $(".publish_button").click(function(){
            if (confirm("This will make your piece available to the general public.  There's no undo, but it is pretty awesome.  Ready to go?")) {
                $("#id_is_draft").val("False");
                $(".poem_form").submit();
            }
            return false;
        });
        $(".start_editing_button").click(Poemhub.poem.editor.start_editing);
        $(".cancel_editing_button").click(Poemhub.poem.editor.cancel_editing);
        $(".options_button").click(Poemhub.poem.editor.toggle_options);
        $(".fantastic_button").click(Poemhub.poem.toggle_fantastic);
        if (window.location.href.indexOf("?editing=true") != -1) {
            Poemhub.poem.editor.start_editing();
        }
        bkLib.onDomLoaded(nicEditors.allTextAreas);
    };
    Poemhub.poem.actions.init();

});
