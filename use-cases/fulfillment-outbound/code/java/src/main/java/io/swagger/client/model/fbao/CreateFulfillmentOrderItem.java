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
import io.swagger.client.model.fbao.Money;
import java.io.IOException;

/**
 * Item information for creating a fulfillment order.
 */
@ApiModel(description = "Item information for creating a fulfillment order.")
@javax.annotation.Generated(value = "io.swagger.codegen.languages.JavaClientCodegen", date = "2023-10-17T21:02:37.663-07:00")
public class CreateFulfillmentOrderItem {
  @SerializedName("sellerSku")
  private String sellerSku = null;

  @SerializedName("sellerFulfillmentOrderItemId")
  private String sellerFulfillmentOrderItemId = null;

  @SerializedName("quantity")
  private Integer quantity = null;

  @SerializedName("giftMessage")
  private String giftMessage = null;

  @SerializedName("displayableComment")
  private String displayableComment = null;

  @SerializedName("fulfillmentNetworkSku")
  private String fulfillmentNetworkSku = null;

  @SerializedName("perUnitDeclaredValue")
  private Money perUnitDeclaredValue = null;

  @SerializedName("perUnitPrice")
  private Money perUnitPrice = null;

  @SerializedName("perUnitTax")
  private Money perUnitTax = null;

  public CreateFulfillmentOrderItem sellerSku(String sellerSku) {
    this.sellerSku = sellerSku;
    return this;
  }

   /**
   * The seller SKU of the item.
   * @return sellerSku
  **/
  @ApiModelProperty(required = true, value = "The seller SKU of the item.")
  public String getSellerSku() {
    return sellerSku;
  }

  public void setSellerSku(String sellerSku) {
    this.sellerSku = sellerSku;
  }

  public CreateFulfillmentOrderItem sellerFulfillmentOrderItemId(String sellerFulfillmentOrderItemId) {
    this.sellerFulfillmentOrderItemId = sellerFulfillmentOrderItemId;
    return this;
  }

   /**
   * A fulfillment order item identifier that the seller creates to track fulfillment order items. Used to disambiguate multiple fulfillment items that have the same SellerSKU. For example, the seller might assign different SellerFulfillmentOrderItemId values to two items in a fulfillment order that share the same SellerSKU but have different GiftMessage values.
   * @return sellerFulfillmentOrderItemId
  **/
  @ApiModelProperty(required = true, value = "A fulfillment order item identifier that the seller creates to track fulfillment order items. Used to disambiguate multiple fulfillment items that have the same SellerSKU. For example, the seller might assign different SellerFulfillmentOrderItemId values to two items in a fulfillment order that share the same SellerSKU but have different GiftMessage values.")
  public String getSellerFulfillmentOrderItemId() {
    return sellerFulfillmentOrderItemId;
  }

  public void setSellerFulfillmentOrderItemId(String sellerFulfillmentOrderItemId) {
    this.sellerFulfillmentOrderItemId = sellerFulfillmentOrderItemId;
  }

  public CreateFulfillmentOrderItem quantity(Integer quantity) {
    this.quantity = quantity;
    return this;
  }

   /**
   * Get quantity
   * @return quantity
  **/
  @ApiModelProperty(required = true, value = "")
  public Integer getQuantity() {
    return quantity;
  }

  public void setQuantity(Integer quantity) {
    this.quantity = quantity;
  }

  public CreateFulfillmentOrderItem giftMessage(String giftMessage) {
    this.giftMessage = giftMessage;
    return this;
  }

   /**
   * A message to the gift recipient, if applicable.
   * @return giftMessage
  **/
  @ApiModelProperty(value = "A message to the gift recipient, if applicable.")
  public String getGiftMessage() {
    return giftMessage;
  }

  public void setGiftMessage(String giftMessage) {
    this.giftMessage = giftMessage;
  }

  public CreateFulfillmentOrderItem displayableComment(String displayableComment) {
    this.displayableComment = displayableComment;
    return this;
  }

   /**
   * Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.
   * @return displayableComment
  **/
  @ApiModelProperty(value = "Item-specific text that displays in recipient-facing materials such as the outbound shipment packing slip.")
  public String getDisplayableComment() {
    return displayableComment;
  }

  public void setDisplayableComment(String displayableComment) {
    this.displayableComment = displayableComment;
  }

  public CreateFulfillmentOrderItem fulfillmentNetworkSku(String fulfillmentNetworkSku) {
    this.fulfillmentNetworkSku = fulfillmentNetworkSku;
    return this;
  }

   /**
   * Amazon&#39;s fulfillment network SKU of the item.
   * @return fulfillmentNetworkSku
  **/
  @ApiModelProperty(value = "Amazon's fulfillment network SKU of the item.")
  public String getFulfillmentNetworkSku() {
    return fulfillmentNetworkSku;
  }

  public void setFulfillmentNetworkSku(String fulfillmentNetworkSku) {
    this.fulfillmentNetworkSku = fulfillmentNetworkSku;
  }

  public CreateFulfillmentOrderItem perUnitDeclaredValue(Money perUnitDeclaredValue) {
    this.perUnitDeclaredValue = perUnitDeclaredValue;
    return this;
  }

   /**
   * The monetary value assigned by the seller to this item.
   * @return perUnitDeclaredValue
  **/
  @ApiModelProperty(value = "The monetary value assigned by the seller to this item.")
  public Money getPerUnitDeclaredValue() {
    return perUnitDeclaredValue;
  }

  public void setPerUnitDeclaredValue(Money perUnitDeclaredValue) {
    this.perUnitDeclaredValue = perUnitDeclaredValue;
  }

  public CreateFulfillmentOrderItem perUnitPrice(Money perUnitPrice) {
    this.perUnitPrice = perUnitPrice;
    return this;
  }

   /**
   * The amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.
   * @return perUnitPrice
  **/
  @ApiModelProperty(value = "The amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.")
  public Money getPerUnitPrice() {
    return perUnitPrice;
  }

  public void setPerUnitPrice(Money perUnitPrice) {
    this.perUnitPrice = perUnitPrice;
  }

  public CreateFulfillmentOrderItem perUnitTax(Money perUnitTax) {
    this.perUnitTax = perUnitTax;
    return this;
  }

   /**
   * The tax on the amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.
   * @return perUnitTax
  **/
  @ApiModelProperty(value = "The tax on the amount to be collected from the recipient for this item in a COD (Cash On Delivery) order.")
  public Money getPerUnitTax() {
    return perUnitTax;
  }

  public void setPerUnitTax(Money perUnitTax) {
    this.perUnitTax = perUnitTax;
  }


  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    CreateFulfillmentOrderItem createFulfillmentOrderItem = (CreateFulfillmentOrderItem) o;
    return Objects.equals(this.sellerSku, createFulfillmentOrderItem.sellerSku) &&
        Objects.equals(this.sellerFulfillmentOrderItemId, createFulfillmentOrderItem.sellerFulfillmentOrderItemId) &&
        Objects.equals(this.quantity, createFulfillmentOrderItem.quantity) &&
        Objects.equals(this.giftMessage, createFulfillmentOrderItem.giftMessage) &&
        Objects.equals(this.displayableComment, createFulfillmentOrderItem.displayableComment) &&
        Objects.equals(this.fulfillmentNetworkSku, createFulfillmentOrderItem.fulfillmentNetworkSku) &&
        Objects.equals(this.perUnitDeclaredValue, createFulfillmentOrderItem.perUnitDeclaredValue) &&
        Objects.equals(this.perUnitPrice, createFulfillmentOrderItem.perUnitPrice) &&
        Objects.equals(this.perUnitTax, createFulfillmentOrderItem.perUnitTax);
  }

  @Override
  public int hashCode() {
    return Objects.hash(sellerSku, sellerFulfillmentOrderItemId, quantity, giftMessage, displayableComment, fulfillmentNetworkSku, perUnitDeclaredValue, perUnitPrice, perUnitTax);
  }


  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class CreateFulfillmentOrderItem {\n");
    
    sb.append("    sellerSku: ").append(toIndentedString(sellerSku)).append("\n");
    sb.append("    sellerFulfillmentOrderItemId: ").append(toIndentedString(sellerFulfillmentOrderItemId)).append("\n");
    sb.append("    quantity: ").append(toIndentedString(quantity)).append("\n");
    sb.append("    giftMessage: ").append(toIndentedString(giftMessage)).append("\n");
    sb.append("    displayableComment: ").append(toIndentedString(displayableComment)).append("\n");
    sb.append("    fulfillmentNetworkSku: ").append(toIndentedString(fulfillmentNetworkSku)).append("\n");
    sb.append("    perUnitDeclaredValue: ").append(toIndentedString(perUnitDeclaredValue)).append("\n");
    sb.append("    perUnitPrice: ").append(toIndentedString(perUnitPrice)).append("\n");
    sb.append("    perUnitTax: ").append(toIndentedString(perUnitTax)).append("\n");
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

