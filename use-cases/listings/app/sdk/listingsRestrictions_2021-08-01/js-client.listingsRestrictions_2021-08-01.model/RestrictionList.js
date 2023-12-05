/*
 * Selling Partner API for Listings Restrictions
 * The Selling Partner API for Listings Restrictions provides programmatic access to restrictions on Amazon catalog listings.  For more information, see the [Listings Restrictions API Use Case Guide](doc:listings-restrictions-api-v2021-08-01-use-case-guide).
 *
 * OpenAPI spec version: 2021-08-01
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 *
 * Swagger Codegen version: 2.4.9
 *
 * Do not edit the class manually.
 *
 */

import { ApiClient } from "../ApiClient.js";
import { Restriction } from "./Restriction.js";

/**
 * The RestrictionList model module.
 * @module listingsRestrictions_2021-08-01/js-client.listingsRestrictions_2021-08-01.model/RestrictionList
 * @version 2021-08-01
 */
export class RestrictionList {
  /**
   * Constructs a new <code>RestrictionList</code>.
   * A list of restrictions for the specified Amazon catalog item.
   * @alias module:listingsRestrictions_2021-08-01/js-client.listingsRestrictions_2021-08-01.model/RestrictionList
   * @class
   * @param restrictions {Array.<module:listingsRestrictions_2021-08-01/js-client.listingsRestrictions_2021-08-01.model/Restriction>}
   */
  constructor(restrictions) {
    this.restrictions = restrictions;
  }

  /**
   * Constructs a <code>RestrictionList</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:listingsRestrictions_2021-08-01/js-client.listingsRestrictions_2021-08-01.model/RestrictionList} obj Optional instance to populate.
   * @return {module:listingsRestrictions_2021-08-01/js-client.listingsRestrictions_2021-08-01.model/RestrictionList} The populated <code>RestrictionList</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new RestrictionList();
      if (data.hasOwnProperty("restrictions"))
        obj.restrictions = ApiClient.convertToType(data["restrictions"], [
          Restriction,
        ]);
    }
    return obj;
  }
}

/**
 * @member {Array.<module:listingsRestrictions_2021-08-01/js-client.listingsRestrictions_2021-08-01.model/Restriction>} restrictions
 */
RestrictionList.prototype.restrictions = undefined;