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
 * The request schema for the createDestination operation.
 */
@ApiModel(description = "The request schema for the createDestination operation.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2021-11-24T16:14:21.819+01:00")
public class CreateDestinationRequest {
  @SerializedName("resourceSpecification")
  private DestinationResourceSpecification resourceSpecification = null;

  @SerializedName("name")
  private String name = null;

  public CreateDestinationRequest resourceSpecification(DestinationResourceSpecification resourceSpecification) {
    this.resourceSpecification = resourceSpecification;
    return this;
  }

   /**
   * The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.
   * @return resourceSpecification
  **/
  @ApiModelProperty(required = true, value = "The information required to create a destination resource. Applications should use one resource type (sqs or eventBridge) per destination.")
  public DestinationResourceSpecification getResourceSpecification() {
    return resourceSpecification;
  }

  public void setResourceSpecification(DestinationResourceSpecification resourceSpecification) {
    this.resourceSpecification = resourceSpecification;
  }

  public CreateDestinationRequest name(String name) {
    this.name = name;
    return this;
  }

   /**
   * A developer-defined name to help identify this destination.
   * @return name
  **/
  @ApiModelProperty(required = true, value = "A developer-defined name to help identify this destination.")
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }


  @Override
  public boolean equals(Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateDestinationRequest createDestinationRequest = (CreateDestinationRequest) o;
    return Objects.equals(this.resourceSpecification, createDestinationRequest.resourceSpecification) &&
        Objects.equals(this.name, createDestinationRequest.name);
  }

  @Override
  public int hashCode() {
    return Objects.hash(resourceSpecification, name);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateDestinationRequest {\n");
    
    sb.append("    resourceSpecification: ").append(toIndentedString(resourceSpecification)).append("\n");
    sb.append("    name: ").append(toIndentedString(name)).append("\n");
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

