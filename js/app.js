Vue.component('function-instance', {
    props: ['instance', 'onEdit'],
    template: "#tmpl-function-instance",
    computed: {
        fDef: function() {
            console.log(this.instance.fDef);
            return window.fDefs[this.instance.fDef];
        }, 
        output: function() {
            return window.fDefs[this.instance.fDef].func(this.instance.args);
        }
    }, 
    methods: {
        toggleEdit: function() {
            this.onEdit(this.instance.id);
        }
    }
})


TYPES = ["String", "Number", "Boolean", "Function", "Object", "Array", "Reference"]

window.fDefs = [
    {
        "id": 1,
        "name": "Number", 
        "parameters": [
            {
                "name": "Value", 
                "type": "number"
            }
        ], 
        func: function(args) {
            return args["Value"];
        }
    },
    {"name": "Add", "id": 2},
];

window.currentEdit = -1;
window.maxInstanceId = 1;

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        functionDefinitions: window.fDefs, 
        instances: [
            {
                "id": 0, 
                "fDef": 0, 
                "name": "random name", 
                args: {"Value": 5}, 
                isEdit: false
            }
        ]
    }, 
    methods: {
        toggleInstanceEdit(index) {
            this.instances[index].isEdit = !this.instances[index].isEdit;
        }
    }
});
