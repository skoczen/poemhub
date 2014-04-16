$(function(){
    // Todo: you know, real code.
    $(".fantastic_button").click(function(){
        $(this).toggleClass("clicked");
    });
    $(".toggle_editing_button").click(function(){
        $(".edit_bar").toggleClass("editing");
    });
});
