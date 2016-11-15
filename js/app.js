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


Vue.component('key-value-list', {
    template: "#tmpl-key-val", 
    data: function() {
        return {
            "items": [
                {"key": "item 1", "value": "val 1"},
                {"key": "item 2", "value": "val 2"},
            ],
            "newkey": "",
            "newvalue": ""
        }
    },
    methods: {
        addAndFocus: function(selector) {
            this.items.push({"key": this.newkey, "value": this.newvalue})
            
            // 
            this.newkey = "";
            this.newvalue = "";
            
            Vue.nextTick(function () {
                let valueInputs = document.querySelectorAll(selector);
                valueInputs[valueInputs.length - 1].focus();
            });

        },
        addNewKey: function(evnt) {
            this.addAndFocus(".inKey");
        },
        addNewValue: function(evnt) {
            this.addAndFocus(".inVal");
        }
    }
})


Vue.component('dynamic-table', {
    template: "#tmpl-dynamic-table",
    data: function() {
        return {
            "columns": ["date", 
                        "source", 
                        "new customer", 
                        "customer", 
                        "items", 
                        "quantity"],
            "rows": [
                {
                    "id": 1,
                    "date": "2016/05/10",
                    "source": "internet",
                    "customer": "",
                    "new customer": "Yes",
                    "items": ["Item 1", "Item 2"], 
                    "quantity": [3, 5, 7]
                },
                {
                    "id": 2,
                    "date": "2016/07/10",
                    "source": "walkin",
                    "new customer": "No",
                    "customer": "Bob",
                    "items": ["Item 1"], 
                    "quantity": [1]
                }
            ],
            "selected": {
                "path": {},
                "x": 132,
                "y": 99,
                "width": 20,
                "height": 20,
                "active": false,
                "value": ""
            }
        }
    }, 
    computed: {
        renderedTable: function() {
            let renderedRows = [];
            for(var r = 0; r < this.rows.length; r++){
                // let row = [];
                let rowspan = 1;
                // Compute rowspan
                for(var c = 0; c < this.columns.length; c++){
                    let columnVal = this.rows[r][this.columns[c]];
                    if(columnVal instanceof Array){
                        if(columnVal.length >= rowspan) {
                            rowspan = columnVal.length + 1;
                        }
                    }
                }
                
                for(var rowId = 0; rowId < rowspan; rowId++) {
                    let currentRow = [];
                    if(rowId === 0){
                        currentRow.push({rowspan: rowspan, value: r + 1, "header": true});
                    }
                    
                    for(var c = 0; c < this.columns.length; c++){
                        let columnName = this.columns[c];
                        let columnVal = this.rows[r][columnName];
                        if(columnVal instanceof Array){
                            if(rowId < columnVal.length){
                                let value = columnVal[rowId]
                                currentRow.push({
                                    "rowspan": 1,
                                    "value": value,
                                    "path": {
                                        "id": r,
                                        columnName: value,
                                        "_next": {
                                            "_index": rowId
                                        },
                                        "_row": "id",
                                        "_col": columnName
                                    }
                                })
                            } else if (rowId === columnVal.length) {
                                currentRow.push({
                                    "rowspan": rowspan - columnVal.length,
                                    "value": "",
                                    "path": {
                                        "id": r,
                                        columnName: "",
                                        "_next": {
                                            "_index": rowId
                                        },
                                        "_row": "id",
                                        "_col": columnName
                                    }
                                })
                            }
                        }
                        else {
                            if(rowId === 0){
                                currentRow.push({
                                    "rowspan": rowspan, 
                                    "value": columnVal,
                                    "path": {
                                        "id": r,
                                        columnName: columnVal,
                                        "_row": "id",
                                        "_col": columnName
                                    }
                                });
                            }
                        }
                    }
                    renderedRows.push(currentRow);
                }
                // renderedRows.push(row);
            }
            return renderedRows;
        }
    },
    methods: {
        addRow: function(){
            let newObject = {};
            for(var i = 0; i < this.columns.length; i++){
                // TODO: Append the appropriate zero value for each row
                newObject[this.columns[i]] = ""
            }
            this.rows.append(newObject)
        },
        setItem: function(path, value) {
            console.log(path);
            // TODO: This should eventually work for infinitely nested objects.
            let row = path["id"];
            let col = path["_col"];
            console.log(path["_next"] !== undefined);
            if (path["_next"] !== undefined){
                let index = path["_next"]["_index"]
                // Have to do it this way to force it to update properly
                var arrClone = this.rows[row][col].slice(0);
                arrClone[index] = value;
                // If you clear out the last value, then the cell goes away
                if (index == arrClone.length -1 && value == "") {
                    arrClone.pop()
                }
                this.rows[row][col] = arrClone;
                
            } else {
                this.rows[row][col] = value;
            }
                
        },
        select: function(col, event) {
            console.log(col);
            console.log(event);
            window.evt = event;
            if(this.selected.active){
                // Save the existing value
                this.setItem(this.selected.path, this.selected.value);
            }
            
            this.selected.active = true;
            this.selected.x = event.target.offsetLeft;
            this.selected.y = event.target.offsetTop;
            this.selected.width = event.target.offsetWidth;
            this.selected.height = event.target.offsetHeight;
            
            this.selected.path = col.path;
            this.selected.value = col.value;
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
        "name": "Multiply",
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
         return args["a"] * args["b"];
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
                "isEdit": true
            }
            instances.push(newInstance);
            // this.instances.push(newInstance);
        }
    }
});
