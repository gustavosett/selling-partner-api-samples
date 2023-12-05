/*
 * Selling Partner API for Notifications
 * The Selling Partner API for Notifications lets you subscribe to notifications that are relevant to a selling partner's business. Using this API you can create a destination to receive notifications, subscribe to notifications, delete notification subscriptions, and more.  For more information, see the [Notifications Use Case Guide](doc:notifications-api-v1-use-case-guide).
 *
 * OpenAPI spec version: v1
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
import { ProcessingDirective } from "./ProcessingDirective.js";

/**
 * The CreateSubscriptionRequest model module.
 * @module notifications/js-client.notifications.model/CreateSubscriptionRequest
 * @version v1
 */
export class CreateSubscriptionRequest {
  /**
   * Constructs a new <code>CreateSubscriptionRequest</code>.
   * The request schema for the createSubscription operation.
   * @alias module:notifications/js-client.notifications.model/CreateSubscriptionRequest
   * @class
   */
  constructor() {}

  /**
   * Constructs a <code>CreateSubscriptionRequest</code> from a plain JavaScript object, optionally creating a new instance.
   * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
   * @param {Object} data The plain JavaScript object bearing properties of interest.
   * @param {module:notifications/js-client.notifications.model/CreateSubscriptionRequest} obj Optional instance to populate.
   * @return {module:notifications/js-client.notifications.model/CreateSubscriptionRequest} The populated <code>CreateSubscriptionRequest</code> instance.
   */
  static constructFromObject(data, obj) {
    if (data) {
      obj = obj || new CreateSubscriptionRequest();
      if (data.hasOwnProperty("payloadVersion"))
        obj.payloadVersion = ApiClient.convertToType(
          data["payloadVersion"],
          "String",
        );
      if (data.hasOwnProperty("destinationId"))
        obj.destinationId = ApiClient.convertToType(
          data["destinationId"],
          "String",
        );
      if (data.hasOwnProperty("processingDirective"))
        obj.processingDirective = ProcessingDirective.constructFromObject(
          data["processingDirective"],
        );
    }
    return obj;
  }
}

/**
 * The version of the payload object to be used in the notification.
 * @member {String} payloadVersion
 */
CreateSubscriptionRequest.prototype.payloadVersion = undefined;

/**
 * The identifier for the destination where notifications will be delivered.
 * @member {String} destinationId
 */
CreateSubscriptionRequest.prototype.destinationId = undefined;

/**
 * @member {module:notifications/js-client.notifications.model/ProcessingDirective} processingDirective
 */
CreateSubscriptionRequest.prototype.processingDirective = undefined;