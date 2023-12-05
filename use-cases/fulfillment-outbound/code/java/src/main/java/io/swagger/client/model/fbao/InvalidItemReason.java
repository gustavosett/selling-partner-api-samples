/*
 * Selling Partner APIs for Fulfillment Outbound
 * The Selling Partner API for Fulfillment Outbound lets you create applications that help a seller fulfill Multi-Channel Fulfillment orders using their inventory in Amazon's fulfillment network. You can get information on both potential and existing fulfillment orders.
 *
 * OpenAPI spec version: 2020-07-01
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */


package io.swagger.client.model.fbao;

import java.util.Objects;
import java.util.Arrays;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import io.swagger.client.model.fbao.InvalidItemReasonCode;
import java.io.IOException;

/**
 * The reason that the item is invalid for return.
 */
@ApiModel(description = "The reason that the item is invalid for return.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2023-10-17T21:02:37.663-07:00")
public class InvalidItemReason {
  @SerializedName("invalidItemReasonCode")
  private InvalidItemReasonCode invalidItemReasonCode = null;

  @SerializedName("description")
  private String description = null;

  public InvalidItemReason invalidItemReasonCode(InvalidItemReasonCode invalidItemReasonCode) {
    this.invalidItemReasonCode = invalidItemReasonCode;
    return this;
  }

   /**
   * Get invalidItemReasonCode
   * @return invalidItemReasonCode
  **/
  @ApiModelProperty(required = true, value = "")
  public InvalidItemReasonCode getInvalidItemReasonCode() {
    return invalidItemReasonCode;
  }

  public void setInvalidItemReasonCode(InvalidItemReasonCode invalidItemReasonCode) {
    this.invalidItemReasonCode = invalidItemReasonCode;
  }

  public InvalidItemReason description(String description) {
    this.description = description;
    return this;
  }

   /**
   * A human readable description of the invalid item reason code.
   * @return description
  **/
  @ApiModelProperty(required = true, value = "A human readable description of the invalid item reason code.")
  public String getDescription() {
    return description;
  }

  public void setDescription(String description) {
    this.description = description;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InvalidItemReason invalidItemReason = (InvalidItemReason) o;
    return Objects.equals(this.invalidItemReasonCode, invalidItemReason.invalidItemReasonCode) &&
        Objects.equals(this.description, invalidItemReason.description);
  }

  @Override
  public int hashCode() {
    return Objects.hash(invalidItemReasonCode, description);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InvalidItemReason {\n");
    
    sb.append("    invalidItemReasonCode: ").append(toIndentedString(invalidItemReasonCode)).append("\n");
    sb.append("    description: ").append(toIndentedString(description)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}

