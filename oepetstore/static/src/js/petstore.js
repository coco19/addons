openerp.oepetstore = function(instance, local) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    local.HomePage = instance.Widget.extend({
        className: 'oe_petstore_homepage',
        start: function() {
            //console.log("pet store home page loaded");
	    this.$el.append("<div>Hello dear Odoo user!</div>");
            var greeting = new local.GreetingsWidget(this);
            //muestra por consola los widgets hijos de este
            console.log(this.getChildren()[0].$el);
            return greeting.appendTo(this.$el);
        },
    });
    
    local.GreetingsWidget = instance.Widget.extend({
        className: 'oe_petstore_greetings',
        start: function() {
            this.$el.append("<div>We are so happy to see you again in this menu!</div>");
            // el codigo siguiente muestra por consola el widget padre de este widget
            console.log(this.getParent().$el );
        },
    });


    instance.web.client_actions.add('petstore.homepage', 'instance.oepetstore.HomePage');
}
