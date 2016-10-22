var instances = [
    {
        "id": 0,
        "fDef": 0,
        "name": "random name",
        args: {"Value": 5},
        isEdit: true
    }
];

Vue.component('function-instance', {
    props: ['instance', 'onEdit'],
    template: "#tmpl-function-instance",
    data: function() {
        return instances[this.instance.id];
    },
    computed: {
        fDef: function() {
            return window.fDefs[this.instance.fDef];
        }
    }, 
    methods: {
        toggleEdit: function() {
            this.onEdit(this.instance.id);
        },
        saveEdit: function() {
            this.onEdit(this.instance.id);
        },
        output: function() {
            return window.fDefs[this.instance.fDef].func(this.args);
        }
    }
})


TYPES = ["String", "Number", "Boolean", "Function", "Object", "Array", "Reference"]

window.fDefs = [
    {
        "id": 0,
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
    {
        "id": 1,
        "name": "Add",
        "parameters": [
            {
                "name": "a",
                "type": "number"
            },
            {
                "name": "b",
                "type": "number"
            }
    ], 
     func: function(args) {
         console.log(args);
         return args["a"] + args["b"];
     }
    },
];

window.currentEdit = -1;
window.maxInstanceId = 1;

var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue!',
        functionDefinitions: window.fDefs, 
        instances: instances,
        newFuncId: 0
    }, 
    methods: {
        toggleInstanceEdit(index) {
            console.log(this.instances[index]);
            this.instances[index].isEdit = !this.instances[index].isEdit;
        }, 
        showAddInstance() {
            console.log("show add instance");
            console.log(this.newFuncId);
            let newInstance = {
                "id": window.maxInstanceId++,
                "fDef": this.newFuncId,
                "name": "New Function",
                "args": {},
                "isEdit": false
            }
            instances.push(newInstance);
            // this.instances.push(newInstance);
        }
    }
});
