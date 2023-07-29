var MyQueue = function() {
    this.first = [];
    this.last = [];
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    const length = this.first.length;
    for(var i = 0; i < length; i++) {
        this.last.push(this.first.pop());
    }
    this.last.push(x);
    return this
};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    const length = this.last.length;
    for (let i = 0; i < length; i++) {
        this.first.push(this.last.pop());
    }
    return this.first.pop();
    // return this;
    // this.last.push(this.first.pop());
    // return this.first[this.first.length - 1];
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    if (this.last.length > 0) {
        return this.last[0];
    }
    return this.first[this.first.length - 1];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    if(this.first.length === 0 && this.last.length === 0) {
        return true;
    }
    return false;
};

/** 
 * Your MyQueue object will be instantiated and called as such:
 * var obj = new MyQueue()
 * obj.push(x)
 * var param_2 = obj.pop()
 * var param_3 = obj.peek()
 * var param_4 = obj.empty()
 */