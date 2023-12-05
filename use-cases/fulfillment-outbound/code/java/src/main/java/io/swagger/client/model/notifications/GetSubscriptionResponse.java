/*
 * Selling Partner API for Notifications
 * The Selling Partner API for Notifications lets you subscribe to notifications that are relevant to a selling partner's business. Using this API you can create a destination to receive notifications, subscribe to notifications, delete notification subscriptions, and more.
 *
 * OpenAPI spec version: v1
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model.notifications;

import java.util.Objects;

import com.google.gson.annotations.SerializedName;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;

/**
 * The response schema for the getSubscription operation.
 */
@ApiModel(description = "The response schema for the getSubscription operation.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2021-11-24T16:14:21.819+01:00")
public class GetSubscriptionResponse {
  @SerializedName("payload")
  private Subscription payload = null;

  @SerializedName("errors")
  private ErrorList errors = null;

  public GetSubscriptionResponse payload(Subscription payload) {
    this.payload = payload;
    return this;
  }

   /**
   * The payload for the getSubscription operation.
   * @return payload
  **/
  @ApiModelProperty(value = "The payload for the getSubscription operation.")
  public Subscription getPayload() {
    return payload;
  }

  public void setPayload(Subscription payload) {
    this.payload = payload;
  }

  public GetSubscriptionResponse errors(ErrorList errors) {
    this.errors = errors;
    return this;
  }

   /**
   * One or more unexpected errors occurred during the getSubscription operation.
   * @return errors
  **/
  @ApiModelProperty(value = "One or more unexpected errors occurred during the getSubscription operation.")
  public ErrorList getErrors() {
    return errors;
  }

  public void setErrors(ErrorList errors) {
    this.errors = errors;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    GetSubscriptionResponse getSubscriptionResponse = (GetSubscriptionResponse) o;
    return Objects.equals(this.payload, getSubscriptionResponse.payload) &&
        Objects.equals(this.errors, getSubscriptionResponse.errors);
  }

  @Override
  public int hashCode() {
    return Objects.hash(payload, errors);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetSubscriptionResponse {\n");
    
    sb.append("    payload: ").append(toIndentedString(payload)).append("\n");
    sb.append("    errors: ").append(toIndentedString(errors)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

