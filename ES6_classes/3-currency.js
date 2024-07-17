export default class Currency {
  constructor(code, name) {
    this._code = this.validateString(code, 'Code');
    this._name = this.validateString(name, 'Name');
  }

  validateString(value, attribute) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attribute} must be a string`);
    }
    return value;
  }

  get code() {
    return this._code;
  }

  set code(value) {
    this._code = this.validateString(value, 'Code');
  }

  get name() {
    return this._name;
  }

  set name(value) {
    this._name = this.validateString(value, 'Name');
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
