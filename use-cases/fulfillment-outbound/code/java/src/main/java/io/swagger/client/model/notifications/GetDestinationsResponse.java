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
 * The response schema for the getDestinations operation.
 */
@ApiModel(description = "The response schema for the getDestinations operation.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2021-11-24T16:14:21.819+01:00")
public class GetDestinationsResponse {
  @SerializedName("payload")
  private DestinationList payload = null;

  @SerializedName("errors")
  private ErrorList errors = null;

  public GetDestinationsResponse payload(DestinationList payload) {
    this.payload = payload;
    return this;
  }

   /**
   * The payload for the getDestinations operation.
   * @return payload
  **/
  @ApiModelProperty(value = "The payload for the getDestinations operation.")
  public DestinationList getPayload() {
    return payload;
  }

  public void setPayload(DestinationList payload) {
    this.payload = payload;
  }

  public GetDestinationsResponse errors(ErrorList errors) {
    this.errors = errors;
    return this;
  }

   /**
   * One or more unexpected errors occurred during the getDestinations operation.
   * @return errors
  **/
  @ApiModelProperty(value = "One or more unexpected errors occurred during the getDestinations operation.")
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
    GetDestinationsResponse getDestinationsResponse = (GetDestinationsResponse) o;
    return Objects.equals(this.payload, getDestinationsResponse.payload) &&
        Objects.equals(this.errors, getDestinationsResponse.errors);
  }

  @Override
  public int hashCode() {
    return Objects.hash(payload, errors);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class GetDestinationsResponse {\n");
    
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

