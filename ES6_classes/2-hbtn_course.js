export default class HolbertonCourse
  constructor(name, length, students) {
    this._name =
    this._length =
    this._students =
  }

  validateString(value, attribute) {
    if (typeof value !== 'string') {
      throw new TypeError(`${attribute} must be a string`);
    }
    return value;
  }

  validateNumber(value, attribute) {
    if (typeof value !== 'number') {
      throw new TypeError(`${attribute} must be a number`);
    }
    return value;
  }

  validateArray(value, attribute) {
    if (!Array.isArray(value)) {
      throw new TypeError(`${attribute} must be an array`);
    }
    for (const item of value) {
      if (typeof item !== 'string') {
        throw new TypeError(`Each element in ${attribute} must be a string`);
      }
    }
    return value;
  }
