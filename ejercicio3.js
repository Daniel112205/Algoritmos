class Queue{
    constructor() { 
        this.items = Array.prototype.slice.call(arguments, 0);
        this.limit = 10;
    }
    
    add(e) {
        if(this.items.length < this.limit){
            this.items.push(e);
            return true;
        }
        return false;
    }

    element(){
        return this.items[0];
    }

    is_empty(){
        return this.items.length == 0;
    }

    size(){
        return this.items.length;
    }
}

let queue = new Queue();

console.log(queue.is_empty());
queue.add(10);
queue.add(11);
queue.add(12);
queue.add(13);
queue.add(14);
queue.add(15);
queue.add(16);
queue.add(17);
queue.add(18);
queue.add(19);
console.log(queue.element());
console.log(queue.size());